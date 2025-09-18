import pytest
from homework1.src.task4 import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 10) == 90.0
    assert calculate_discount(200, 25) == 150.0
    assert calculate_discount(100.0, 10.0) == 90.0

def test_invalid_price_type():
    # Price should be int/float, not string
    with pytest.raises(TypeError):
        calculate_discount("100", 10)

def test_invalid_discount_type():
    # Discount should be int/float, not string
    with pytest.raises(TypeError):
        calculate_discount(100, "10")

def test_negative_discount():
    # Discount < 0% invalid
    with pytest.raises(ValueError):
        calculate_discount(100, -5)

def test_excessive_discount():
    # Discount > 100% invalid
    with pytest.raises(ValueError):
        calculate_discount(100, 150)

