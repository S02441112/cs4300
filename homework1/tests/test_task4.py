from homework1.src.task4 import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 10) == 90.0
    assert calculate_discount(200, 25) == 150.0
    assert calculate_discount(100.0, 10.0) == 90.0


