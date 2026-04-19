import hashlib
users = {
    "ali": "123456",
    "ahmad": "password",
    "sara": "qwerty"
}
with open("hashed_passwords.txt", "w") as f:
    for user, pwd in users.items():
        hash_pwd = hashlib.sha256(pwd.encode()).hexdigest()
        f.write(f"{user}:{hash_pwd}\n")
print("Hash file created!")
