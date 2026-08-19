def calculate_product_price(unit_price, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if unit_price < 0:
        raise ValueError("Unit price cannot be negative.")
    return unit_price * quantity


try:
    unit_price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))
    print(f"Total product price: {calculate_product_price(unit_price, quantity)}")
except ValueError as error:
    print(f"Product price error: {error}")
