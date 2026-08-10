old_word = input("Enter old word: ")
new_word = input("Enter new word: ")

with open("files/sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

updated_content = content.replace(old_word, new_word)

with open("files/sample.txt", "w", encoding="utf-8") as file:
    file.write(updated_content)

print("Text replaced successfully.")
