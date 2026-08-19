def read_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied."
    except OSError as error:
        return f"File error: {error}"


file_name = input("Enter file name: ")
print(read_file(file_name))
