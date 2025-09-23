# Homework 1: Introduction to Python & Unit Testing

This project contains solutions for **Homework 1** in CS4300.  
It demonstrates Python basics, control structures, file handling, duck typing, and package usage, with all functionality verified using **pytest**.

---
'''
Project Structure

cs4300/
└── homework1/
├── src/ # Source code for each task
│ ├── task1.py
│ ├── task2.py
│ ├── task3.py
│ ├── task4.py
│ ├── task5.py
│ ├── task6.py
│ └── task7.py
├── tests/ # Unit tests for each task
│ ├── test_task1.py
│ ├── test_task2.py
│ ├── test_task3.py
│ ├── test_task4.py
│ ├── test_task5.py
│ ├── test_task6.py
│ └── test_task7.py
├── task6_read_me.txt # Input text file for Task 6
├── README.md # This file
└── homework2/

'''
# Create and activate a virtual environment

python3 -m venv hw1_venv
source hw1_venv/bin/activate   # Linux/Mac

# Install pytest and Requests (task 7)
pip install pytest
pip install requests


# Run src code
navigate to ~/cs4300/homework1/src
python task1.py   # Replace 1 with the task number

# Running tests 
navigate to ~/cs4300/homework1/tests
export PYTHONPATH="."
pytest test_task1.py	# Replace 1 with the task number

OR run all test at once using:
pytest -vv
