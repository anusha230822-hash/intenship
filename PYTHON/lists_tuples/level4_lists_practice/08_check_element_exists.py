items = ["apple", "banana", "cherry"]
target = "banana"

found = False
for item in items:
    if item == target:
        found = True
        break

print("Found" if found else "Not found")