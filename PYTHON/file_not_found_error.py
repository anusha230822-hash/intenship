file_name = input("Enter the file name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
