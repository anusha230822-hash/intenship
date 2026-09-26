item_price = 100
quantity = 2
tax_rate = 0.18
subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
print("Subtotal:", subtotal, "Tax:", tax, "Total bill:", total)