file_name = input("Enter the numbers file name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        numbers = []
        for line_number, line in enumerate(file, start=1):
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Invalid number on line {line_number}: {line.strip()}")
        print(f"Valid numbers: {numbers}")
except FileNotFoundError:
    print("Error: The numbers file was not found.")
except PermissionError:
    print("Error: Permission denied while reading the file.")
except OSError as error:
    print(f"File error: {error}")
