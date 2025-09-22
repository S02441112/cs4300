# homework1/tests/test_task1.py

from src.task1 import task_1

def test_output():
    """
    Verifies the string "Hello, World!" is returned 
    """
    assert task_1() == "Hello, World!"
