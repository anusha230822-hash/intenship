with open("files/sample.txt", "r", encoding="utf-8") as source:
    content = source.read()

with open("files/copy.txt", "w", encoding="utf-8") as destination:
    destination.write(content)

print("File copied successfully.")
