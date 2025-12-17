def language_skills(person_stats: list) -> int:
    """
    Checks the person's Language skills based on their writing, speaking, listening, and reading scores.
    Also checks if the person has at least a score of 5 in each of the 4 language skills for the second 
    offical language.
    """
    language_points = 0
    for skill in person_stats[4:8]: # Calculating points for primary language
        if skill == "7":
            language_points += 4
        elif skill == "8":
            language_points += 5
        else: # If it's neither, then the score is 9 or higher
            language_points += 6

    # Check if they have at least a score of 5 in each language skill for the second langauge
    if person_stats[8] == "yes":
        language_points += 4

    return language_points

def education_lvl(person_stats: list) -> int:
    """
    Checks the level of education the person has and gives points based on their level of education.
    """
    education_points = 0
    if person_stats[9] == "Secondary school (high school diploma)":
        education_points += 5
    elif person_stats[9] == "One-year degree, diploma or certificate":
        education_points += 15
    elif person_stats[9] == "Two-year degree, diploma or certificate":
        education_points += 19
    elif person_stats[9] == "Bachelor's degree or other programs (three or more years)":
        education_points += 21
    elif person_stats[9] == "Two or more certificates, diplomas, or degrees":
        education_points += 22
    elif person_stats[9] == "Professional degree needed to practice in a licensed profession" or person_stats[9] == "University degree at the Master's level":
        education_points += 23
    else: # Person has a degree at the Doctoral level
        education_points += 25

    return education_points 

def work_experience(person_stats: list) -> int:
    """
    Checks the amount of work experience the person has in years.
    """
    years = int(person_stats[10]) # Convert string into integer
    work_points = 0

    if years >= 6:
        work_points += 15
    elif years >= 4:
        work_points += 13
    elif years >= 2:
        work_points += 11
    elif years == 1: # No work experience gives 0 points, so no need to do a check for that
        work_points += 9

    return work_points

def age_check(person_stats: list) -> int:
    """
    Checks age of the person and gives points accordingly.
    """
    age = int(person_stats[2])
    age_points = 0
    # 0 points are awarded if their age is 47 or older, so no need to check for that age range
    if age >= 18:
        if age <= 35:
            age_points += 12
        elif age == 36:
            age_points += 11
        elif age == 37:
            age_points += 10
        elif age == 38:
            age_points += 9
        elif age == 39:
            age_points += 8
        elif age == 40:
            age_points += 7
        elif age == 41:
            age_points += 6
        elif age == 42:
            age_points += 5
        elif age == 43:
            age_points += 4
        elif age == 44:
            age_points += 3
        elif age == 45:
            age_points += 2
        elif age == 46:
            age_points += 1

    return age_points 

def arranged_employment_check(person_stats: list) -> int:
    """
    Checks if person has an arranged employment and gives 10 points if they do have one.
    """
    employment_points = 0
    if person_stats[11] == "yes": # If no, then they get 0 points
        employment_points += 10
    
    return employment_points

def adaptability(person_stats: list) -> int:
    """
    Checks the adapatability of the person and their spouse (if they have a spouse).
    """
    adapt_points = 0
    for index in range(12, 19): # Goes through columns 13 to 19 (index 12 to 18)
        if person_stats[index] == "yes" or person_stats[index] == "yes\n":
            if index == 16: #17th column (index 16) is the only one that gives 10 points
                adapt_points += 10
            else:
                adapt_points += 5

    return min(adapt_points, 10) # The max amount of points for this secion is 10

def main() -> None:
    """
    Asks the user for the input file they would like to access, as well as the output file accompanying it.
    Displays the number of people qualified, and writes the names of those people into the output file.
    """
    input_file = input("Please provide the name of the input file (to be located in data/input/): ")
    output_file = input("Please provide the name of the output file (to be placed in data/output/): ")

    input_file = open("./data/input/" + input_file, "r") # Mac only detects /, Windows detects both / and \
    output_file = open("./data/output/" + output_file, "w")

    output_file.write("First Name          |Last Name           |  Age|Score\n")
    output_file.write("--------------------+--------------------+-----+-----\n")

    qualified = 0
    for line in input_file:
        if "first_name" not in line: # First line of file is just the name of the columns
            line_list = line.split("\t")
            language_points = language_skills(line_list)
            education_points = education_lvl(line_list)
            work_points = work_experience(line_list)
            age_points = age_check(line_list)
            employment_points = arranged_employment_check(line_list)
            adapt_points = adaptability(line_list)

            # Add all the points together
            total_points = ( # Line is kind of long, had to separate them into different lines
                language_points + 
                education_points + 
                work_points + 
                age_points + 
                employment_points + 
                adapt_points
                )

            if total_points >= 67:
                qualified += 1
                output_file.write(f"{line_list[0]:11}{line_list[1]:10}:\tAGE: {line_list[2]} SCORE: {total_points}\n")

    input_file.close()
    output_file.close()

    print("There were", qualified, "qualified applicants")

main()