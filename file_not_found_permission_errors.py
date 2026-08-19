file_name = input("Enter the file name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Permission denied while opening the file.")
