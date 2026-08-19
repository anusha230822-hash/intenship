def search_dictionary_key(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return "Error: Dictionary key not found."


student = {"name": "Anusha", "course": "Python"}
key = input("Enter dictionary key: ")
print(search_dictionary_key(student, key))
