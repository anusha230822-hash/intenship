is_admin = False
is_manager = True
can_manage_records = is_admin or is_manager
print("Is admin:", is_admin)
print("Is manager:", is_manager)
print("Can manage records:", can_manage_records)