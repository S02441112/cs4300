from homework1.src.task3 import *

def test_sign():
    assert task_3_sign(1) == "Positive"
    assert task_3_sign(-1) == "Negative"
    assert task_3_sign(0) == "Zero"

def test_primes():
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task_3_primes() == expected

def test_sum_numbers():
    assert task_3_sum_numbers() == 5050