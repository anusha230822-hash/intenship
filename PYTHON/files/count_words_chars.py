with open("files/sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

words = content.split()
characters = len(content)

print("Total words:", len(words))
print("Total characters:", characters)
