
def calculate_discount(price, discount):
    """
    Calculate final price after applying discount percentage.
    Demonstrates duck typing (accepts int or float).
    """
    if not (isinstance(price, (int, float)) and isinstance(discount, (int, float))):
        raise TypeError("Both price and discount must be numeric (int or float).")

    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100.")
    else:
        final_price = price - (price * discount / 100)
        print(final_price)
        return float(final_price)


