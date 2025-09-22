import pytest
from src.task3 import *

def test_sign():
    """
    Verify correct identification of number -
    positive, negative, or zero.
    """
    assert task_3_sign(1) == "Positive"
    assert task_3_sign(-1) == "Negative"
    assert task_3_sign(0) == "Zero"

def test_invalid_input_type():
    """
    Passing non-numeric input (string) should raise a TypeError
    """
    # Strings aren’t valid for math comparisons
    with pytest.raises(TypeError):
        task_3_sign("hello")

def test_primes():
    """
    Verify first 10 prime numbers are returned.
    Expected result: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task_3_primes() == expected

def test_sum_numbers():
    """
    Verify sum of integers is returned from 1 to 100 inclusive.
    Formula for sum of first n numbers is n(n+1)/2, so result = 5050.
    """
    assert task_3_sum_numbers() == 5050