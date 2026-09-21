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
│   └── lab5_uml.png                    # 
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
└── requirements.txt                # List of dependencies
```

# Reflections

## 👤 Author
**ALLAN FRITZGERALD N. AMISTOSO** <br>
*2014-73618* <br>
MS Geomatics Engineering - Geoinformatics <br>
University of the Philippines Diliman
