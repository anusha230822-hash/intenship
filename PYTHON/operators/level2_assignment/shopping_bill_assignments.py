product_price = 200
quantity = 5
tax_rate = 0.20
subtotal = product_price * quantity
tax = subtotal * tax_rate
total_bill = subtotal + tax
print("Subtotal:", subtotal, "Tax:", tax, "Total:", total_bill)