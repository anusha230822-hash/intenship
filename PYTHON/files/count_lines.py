count = 0
with open("files/sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        count += 1

print("Total lines:", count)
