purchase_amount = 2500
is_member = True
eligible = purchase_amount >= 2000 and is_member
print("Purchase amount:", purchase_amount)
print("Member:", is_member)
print("Eligible for discount:", eligible)