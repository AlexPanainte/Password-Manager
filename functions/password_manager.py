import json
import os.path
from cryptography.fernet import InvalidToken
import functions.password_encryptor as pe

class PasswordManager:
    def __init__(self):
        self.passwords = []
        self.logged_in = False
        self.username = None
        self.password = None

    def login(self, username, password,encryption_key):
        # Implement a simple login system
        if username == "admin" and password == "password123":
            self.logged_in = True
            self.username = username
            self.password = password
            self.encryption_key=encryption_key
            print("Login successful.")
        else:
            print("Login failed. Invalid username or password.")

    def store_password(self, service, username, password):
        if not self.logged_in:
            print("You must log in to store passwords.")
            return

        # Encrypt the data before storing it
        encryptor = pe.PasswordEncryptor(self.encryption_key)
        encrypted_password = encryptor.encrypt(password.encode()).decode()  # Convert bytes to a string

        entry = {
            "service": service,
            "username": username,
            "password": encrypted_password
        }

        # Load existing passwords
        self.load_passwords()

        # Append the new entry
        self.passwords.append(entry)

        # Save all passwords
        self.save_passwords()

    def retrieve_password(self, service):
        if not self.logged_in:
            print("You must log in to retrieve passwords.")
            return None

        self.load_passwords()
        encryptor = pe.PasswordEncryptor(self.encryption_key)
        for entry in self.passwords:
            if entry["service"] == service:
                try:
                    return encryptor.decrypt(entry["password"].encode())
                except InvalidToken:
                    print("Invalid encryption token. Unable to decrypt the password.")
                    return None
        return None

    def save_passwords(self):
        with open("passwords.json", "w") as f:
            json.dump(self.passwords, f, indent=4)

    def load_passwords(self):
        if os.path.exists("passwords.json"):
            try:
                with open("passwords.json", "r") as f:
                    data = f.read()
                    if data.strip():
                        self.passwords = json.loads(data)
                    else:
                        self.passwords = []
            except (FileNotFoundError, json.JSONDecodeError):
                self.passwords = []
