bill_amount = 1000
discount_rate = 0.20 if bill_amount > 500 else 0.10
discount = bill_amount * discount_rate
final_amount = bill_amount - discount
print("Bill amount:", bill_amount)
print("Final amount:", final_amount)