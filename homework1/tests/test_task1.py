# homework1/tests/test_task1.py

from homework1.src.task1 import task_1

def test_task_1_output(capsys):
    assert task_1() == "Hello, World!"
