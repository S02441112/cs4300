import pytest
from src.task2 import *

@pytest.mark.parametrize(
    "func, expected",
    [
        (task_2_int, 1),                 # integer
        (task_2_float, 9.8),             # float
        (task_2_bool, True),             # boolean
        (task_2_str, "Hello, World!"),   # string
    ]
)

def test_task2(func, expected):
    """
    Parameterized test that checks multiple functions returning
    different Python data types.
    """
    assert func() == expected