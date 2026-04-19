import hashlib
users = {
    "ali": "123456",
    "ahmad": "password",
    "sara": "qwerty"
}
with open("hashed.txt", "w") as f:
    for user, pwd in users.items():
        h = hashlib.md5(pwd.encode()).hexdigest()
        f.write(f"{user}:{h}\n")
print("Done")
