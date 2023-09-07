import json
import os.path
from cryptography.fernet import InvalidToken,Fernet
import functions.password_encryptor as pe

class PasswordManager:
    def __init__(self):
        self.passwords = []
        self.logged_in = False
        self.username = None
        self.password = None

    def generate_encryption_key(self):
        key=Fernet.generate_key()
        return key
    

    def store_account(self, encryption_key,service, username, password):

        encryptor = pe.PasswordEncryptor(encryption_key)
        encrypted_password = encryptor.encrypt(password.encode()).decode()
        
        entry = {
            "service": service,
            "username": username,
            "password": encrypted_password
        }
        print(entry)

        # # Load existing passwords
        # self.load_passwords()

        # # Append the new entry
        # self.passwords.append(entry)

        # # Save all passwords
        # self.save_passwords()

    

    
