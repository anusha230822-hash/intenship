import os

if os.path.exists("files/sample.txt"):
    os.remove("files/sample.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")
