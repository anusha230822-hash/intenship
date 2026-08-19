file_name = input("Enter the file name: ")
file = None

try:
    file = open(file_name, "r", encoding="utf-8")
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("File contents:")
    print(file.read())
finally:
    if file is not None:
        file.close()
    print("File operation finished.")
