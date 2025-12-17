# Federal Skilled Worker Program (FSWP) Applicant Parser

## Overview

This project contains a simple python program that parses through a data file containing applicants for the FSWP and determines if they're eligible. 

The project was completed as part of Assignment 4 for COMP 1701 at Mount Royal University.

## Getting Started

### Prerequisites

Make sure that you've installed [python](https://www.python.org/downloads/) before testing this program out.

### Installation

1. Clone the repo on your local machine:

```bash
git clone https://github.com/nalhe627/FSWP-applicant-parser.git
```

2. Move into the project's root directory:

```bash
cd FSWP-applicant-parser
```

### Run the Program

After [installing](#installation), execute the main file:

```bash
python assign4.py
```

It'll first ask you to enter in one of the input file names from the `data/input/` directory. **You must choose between `dataset-10.txt`, `dataset-100.txt`, or `full-dataset.txt`**

Next, it'll ask you to name the output file of the results, which'll be located in the `data/output` directory. The output will have a table of the applicants from the provided input file that are eligible for the FSWP.
