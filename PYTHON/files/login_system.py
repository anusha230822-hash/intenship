username = input("Create username: ")
password = input("Create password: ")

with open("files/users.txt", "a", encoding="utf-8") as file:
    file.write(f"{username},{password}\n")

print("Registration successful.")
