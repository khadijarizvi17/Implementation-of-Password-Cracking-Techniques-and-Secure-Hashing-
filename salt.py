import hashlib
import os
users = {
    "ali": "123456",
    "ahmad": "password",
    "sara": "qwerty"
}

with open("salted_passwords.txt", "w") as f:
    for user, pwd in users.items():
        salt = os.urandom(16).hex()
        hash_pwd = hashlib.sha256((pwd + salt).encode()).hexdigest()
        f.write(f"{user}:{salt}:{hash_pwd}\n")

print("Salted file created!")
