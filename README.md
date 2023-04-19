# Data Test - Starter Project

### Prerequisites

#### Python (3.8.* or later)

You can install python either [from source](https://www.python.org/downloads/) or [with pyenv](https://github.com/pyenv/pyenv).

Check you have python installed:

```bash
python --version
```

#### Preferably an IDE such as VSCode

https://code.visualstudio.com/Download


### Dependencies and data

#### Creating a virtual environment

Ensure your pip (package manager) is up to date:

```bash
pip install --upgrade pip
```

To check your pip version run:

```bash
pip --version
```

Create the virtual environment in the root of the cloned project:

```bash
python -m venv .venv
```

#### Activating the newly created virtual environment

You always want your virtual environment to be active when working on this project.

```bash
source ./.venv/bin/activate
```

#### Installing Python requirements

This will install some of the packages you might find useful:

```bash
pip install -r requirements.txt
```

#### Running tests to ensure everything is working correctly

```bash
pytest
```

#### Generating the data

A data generator is included as part of the project in `./input_data_generator/main_data_generator.py`
This allows you to generate a configurable number of months of data.

To run the data generator use:

```bash
python ./input_data_generator/main_data_generator.py
```

This should produce customers, products and transaction data under `./input_data/starter`


#### Getting started

The skeleton of a possible solution is provided in `./solution/solution_start.py`
You do not have to use this code if you want to approach the problem in a different way.
