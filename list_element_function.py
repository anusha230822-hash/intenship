def get_list_element(values, index):
    try:
        return values[index]
    except IndexError:
        return "Error: List index is out of range."


values = [10, 20, 30, 40]
try:
    index = int(input("Enter list index: "))
    print(get_list_element(values, index))
except ValueError:
    print("Error: Enter an integer index.")
