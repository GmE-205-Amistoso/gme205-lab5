# Laboratory 5: Object-Oriented Spatial Modeling with UML

## Required Dependencies
Before starting, make sure that you have installed the following dependencies:

- **[Python](https://www.python.org/downloads/) >= 3.14**
- **[pip](https://pip.pypa.io/en/stable/installation/) >= 26.2.1**
- *(Optional)* **[VSCode](https://code.visualstudio.com/)**

# Set up the Virtual Environment

## Create a Python Virtual Environment
Create a Python virtual env (venv):

```bash
python3 -m venv .venv
```

Run the virtual environment:
```bash
source .venv/bin/activate
```

## Install Dependencies
Upgrade pip.

```bash
pip install --upgrade pip
```

Install shapely and pytest
```bash
pip install shapely pytest
```

Save the installed packages.

```bash
pip freeze > requirements.txt
```

## How to run the Python scripts
### Running the runner script
Run the runner script using the following command:

```bash
python3 src/run_lab5.py
```

### Running the test files
Run **test_assessment.py** using the following command:
```bash
python3 -m tests.test_assessment
```
Run **test_rules.py** using the following command:
```bash
python3 -m tests.test_rules
```
Run **test_spatial.py** using the following command:
```bash
python3 -m tests.spatial
```

# Directory Structure
```text
├── diagrams                        # UML Diagrams directory
│   └── lab5_uml.png                    # The class diagram
├── output                          # Output files
│   └── lab4_report.json                # Summary dictionary output from runner script
├── src                             # Source files
│   ├── assessment.py                   # Code for coordinating parcel and a collection of rules
│   ├── demo.py                         # Code for small incremental checks
│   ├── rules.py                        # Code for rule heirarchy
│   ├── run_lab5.py                     # Runner script
│   └── spatial.py                      # Code containing the spatial/domain entities
├── test                            # Verification codes
│   ├── test_assessment.py              # Targeted tests for assessment.py
│   ├── test_rules.py                   # Targeted tests for rules.py
│   └── test_spatial.py                 # Targeted tests for spatial.py
├── README.md                       # This README file
└── requirements.txt                # List of dependencies
```

# The Problem Overview

The aim of this project is to create a system for a local planning team to **evaluate land parcels** against a series of **independent development rules**. For a parcel to be evaluated by the program, it should contain the following four attributes:
* **Identifier** - the unique identifier for each parcel
* **Geometry** - the spatial property of each parcel
* **Zoning Classification** - the assigned zone type of each parcel
* **Area** - the recorded area measurement of each parcel in square meters

Initially, the program should evaluate the parcel by checking the following:
1. **Minimum Area** - this would verify whether a parcel meets a minimum area threshold
2. **Allowed Zones** - this would check if the parcel's zoning classification is within an approved list of allowable zones
3. **Hazard Zone Intersection** - this would check, flag, and reject any parcel that intersects a mapped hazard zone

For the system and design requirements, the program should be able to do the following:
* Each rule must return a result with three elements: the **rule's name, a pass/fail value (boolean), and a text containing the explanation**.
* Running an assessment on a parcel executes all rules and **combines the results into a single report**.
* The program must be structured in a way that it is **scalable**, meaning, new rules (such as checking road-access proximity) can be added without needing to rewrite or modify the core assessment loop.

# Candidate-Class Table
Below is the candidate-class table derived from the problem statement:

| Phrase from problem   | Initial interpretation    | Keep as class?    | Reason                                                    |
| -------------------   | ----------------------    | --------------    | ------                                                    |
| planning team         | actor/stakeholder         | No                | Users of the system but is not part of this small domain problem |
| parcel                | domain entity             | Yes               | Owns parcel identity, state, and geometry behavior.       |
| parcel identifier     | parcel state              | No                | A primitive value owned by the parcel object.             |
| geometry              | parcel state              | No                | A spatial property owned by Parcel.                       |
| zoning classification | parcel state              | No                | A value carried by Parcel. Represented by a library (Shapely). |
| area                  | parcel state              | No                | A numerical constant value carried by Parcel.             |
| minimum area rule     | specialized rule          | Yes               | Has a threshold and one evaluation behavior.              |
| allowable zone rule   | specialized rule          | Yes               | Implements the zoning whitelist checking behavior.        |
| hazard zone           | domain entity             | Yes               | Has its own identity, geometry, type, and severity.       |
| intersecting hazard rule | specialized rule       | Yes               | Performs spatial intersection check between Parcel and Hazard geometries. |
| parcel assessment loop | coordinator              | Yes               | Evaluates a parcel by orchestrating rule execution.       |
| rule result           | value object              | Yes               | Provides one consistent result shape from all rules.      |
| report                | output representation     | Not yet           | A JSON/dict is sufficient for this exercise; a Report class would add little responsibility. |
| program               | application               | No                | Main script entry point or CLI driver rather than a domain model class. |

# UML Diagram
<img src="diagrams/lab5_uml.png" alt="lab5_uml" width="800">

# Reflections

## 👤 Author
**ALLAN FRITZGERALD N. AMISTOSO** <br>
*2014-73618* <br>
MS Geomatics Engineering - Geoinformatics <br>
University of the Philippines Diliman
