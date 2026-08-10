line_number = int(input("Enter line number to update: "))
new_text = input("Enter new text: ")

with open("files/sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

if 1 <= line_number <= len(lines):
    lines[line_number - 1] = new_text + "\n"
    with open("files/sample.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)
    print("Line updated successfully.")
else:
    print("Invalid line number.")
