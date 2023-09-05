import random
import string

class PasswordGenerator:
    def __init__(self):
        pass

    def generate_strong_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        print("Select level of security:\n1. Low\n2. Medium\n3. High")

        while True:
            level = input("").lower()
            if level == "low" or level == "1":
                length = 8
                break
            elif level == "medium" or level == "2":
                length = 16
                break
            elif level == "high" or level == "3":
                length = 20
                break
            else:
                print("Wrong selection! Select level of security again:\n1. Low\n2. Medium\n3. High")

        password = "".join(random.choice(characters) for _ in range(length))
        return password