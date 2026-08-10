with open("files/sample.txt", "r", encoding="utf-8") as first_file:
    content1 = first_file.read()

with open("files/copy.txt", "r", encoding="utf-8") as second_file:
    content2 = second_file.read()

with open("files/merged.txt", "w", encoding="utf-8") as merged_file:
    merged_file.write(content1)
    merged_file.write("\n")
    merged_file.write(content2)

print("Files merged successfully.")
