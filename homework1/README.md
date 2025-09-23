# CS4300 Homework 1: Introduction to Python & Unit Testing

## Project Structure

```
homework1/
|-- src/                   # Source code files
|   |-- task1.py           # Hello World and testing introduction
|   |-- task2.py           # Variables and data types
|   |-- task3.py           # Control structures (if/for/while loops)
|   |-- task4.py           # Functions and duck typing
|   |-- task5.py           # Lists and dictionaries
|   |-- task6.py           # File handling and metaprogramming
|   └-- task7.py           # Package management (requests library)
|-- tests/                 # Test files
|   |-- test_task1.py      # Tests for task1
|   |-- test_task2.py      # Tests for task2
|   |-- test_task3.py      # Tests for task3
|   |-- test_task4.py      # Tests for task4
|   |-- test_task5.py      # Tests for task5
|   |-- test_task6.py      # Tests for task6
|   └-- test_task7.py      # Tests for task7
|-- pyproject.toml         # Contains pytest configuration
|-- task6_read_me.txt      # Text file for task6 file handling
└-- README.md              # This file
```

## Setup Instructions

1. **Create Python Virtual Environment:**
   ```bash
   python3 -m venv homework1_env --system-site-packages
   source homework1_env/bin/activate
   ```

2. **Install required packages:**
   ```bash
   python3 -m pip install pytest numpy
   ```

## Running the Code

### Individual Tasks
Each task can be run independently:

```bash
python task1.py    # Hello World
python task2.py    # Data types demonstration
python task3.py    # Control structures
python task4.py    # Duck typing example
python task5.py    # Lists and dictionaries
python task6.py    # File handling
python task7.py    # Package usage example
```

### Running Tests
Run all tests:
```bash
pytest
```

Run tests for a specific task:
```bash
pytest test_task1.py
pytest test_task2.py -v    # Verbose output
```
## Additional Notes
Development of this readme was assisted by Perplexity AI.