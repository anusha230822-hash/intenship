word = input("Enter a word to search: ")

with open("files/sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

if word.lower() in content.lower():
    print("Word found.")
else:
    print("Word not found.")
