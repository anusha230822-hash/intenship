with open("files/sample.txt", "rb") as source:
    data = source.read()

with open("files/sample_copy.bin", "wb") as destination:
    destination.write(data)

print("Binary file copied successfully.")
