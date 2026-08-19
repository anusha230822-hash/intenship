values = ["Python", "MySQL", "Java"]

try:
    raw_index = input("Enter a list index: ")
    index = int(raw_index)
    print(f"Selected value: {values[index]}")
except ValueError:
    print("Error: Index must be a whole number.")
except IndexError:
    print("Error: Index is outside the list range.")
except TypeError:
    print("Error: The index has an invalid type.")
except Exception as error:
    print(f"Unexpected error: {error}")
