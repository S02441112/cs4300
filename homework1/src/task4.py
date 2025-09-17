
def calculate_discount(price, discount):
    """
    Calculate the final price after applying a discount percentage.

    Args:
        price (int | float): Original price of the product.
        discount (int | float): Discount percentage (0-100).

    Returns:
        float: Final price after discount.
    """
    if not (isinstance(price, (int, float)) and isinstance(discount, (int, float))):
        print("Both price and discount must be numeric (int or float).")

    if discount < 0 or discount > 100:
        print("Discount must be between 0 and 100.")
    else:
        final_price = price - (price * discount / 100)
        print(final_price)
        return float(final_price)


