import json
import os.path
from cryptography.fernet import InvalidToken,Fernet
import functions.password_encryptor as pe

class PasswordManager:
    def __init__(self):
        self.accounts = []
        

    def generate_encryption_key(self):
        key=Fernet.generate_key()
        return key
    
    def save_accounts(self):
        with open("account.json", "a") as f:
            json.dump(self.accounts, f, indent=4)

    def load_accounts(self):
        if os.path.exists("account.json"):
            try:
                with open("account.json", "r") as f:
                    data = f.read()
                    if data.strip():
                        self.passwords = json.loads(data)
                    else:
                        self.passwords = []
            except (FileNotFoundError, json.JSONDecodeError):
                self.passwords = []

    def store_account(self, encryption_key,service, username, password):

        encryptor = pe.PasswordEncryptor(encryption_key)
        encrypted_password = encryptor.encrypt(password.encode()).decode()

        entry = {
            "service": service,
            "username": username,
            "password": encrypted_password
        }
        self.load_accounts()
        self.accounts.append(entry)
        self.save_accounts()

    def get_password(self, service, key):

        self.load_accounts()
        encryptor = pe.PasswordEncryptor(key)
        for entry in self.passwords:
            if entry["service"] == service:
                try:
                    user=entry["username"]
                    decrypted_password = encryptor.decrypt(entry["password"].encode())
                    entry_copy = entry.copy()
                    entry_copy["password"] = decrypted_password
                    account=(f"Username:{user} Password:{decrypted_password}")
                    return account

                except InvalidToken:
                    print("Invalid encryption token. Unable to decrypt the password.")
                    return None
        return None

    

    


