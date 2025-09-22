import pytest
from src.task4 import calculate_discount

def test_calculate_discount():
    """
    Verify calculate_discount applies a discount correctly
    given valid integer and float inputs.
    """
    assert calculate_discount(100, 10) == 90.0
    assert calculate_discount(200, 25) == 150.0
    assert calculate_discount(100.0, 10.0) == 90.0

def test_invalid_price_type():
    """
    Passing a non-numeric price (string) should raise TypeError.
    Price should be int/float, not string.
    """ 
    with pytest.raises(TypeError):
        calculate_discount("100", 10)

def test_invalid_discount_type():
    """
    Passing a non-numeric discount (string) should raise TypeError.
    Discount should be int/float, not string.
    """
    with pytest.raises(TypeError):
        calculate_discount(100, "10")

def test_negative_discount():
    """
    Passing a discount below 0% should raise ValueError.
    """
    # Discount < 0% invalid
    with pytest.raises(ValueError):
        calculate_discount(100, -5)

def test_excessive_discount():
    """
    Passing a discount above 100% should raise ValueError.
    """
    # Discount > 100% invalid
    with pytest.raises(ValueError):
        calculate_discount(100, 150)

def test_discount_zero_percent():
    """
    A 0% discount should return the full original price.
    """
    assert calculate_discount(100, 0) == 100.0

def test_discount_hundred_percent():
    """
    A 100% discount should return 0.0 (free).
    """
    assert calculate_discount(100, 100) == 0.0