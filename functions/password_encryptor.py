from cryptography.fernet import Fernet

class PasswordEncryptor:
    def __init__(self, encryption_key):
        self.encryption_key = encryption_key

    def encrypt(self, data):
        fernet = Fernet(self.encryption_key)
        encrypted_data = fernet.encrypt(data)
        return encrypted_data

    def decrypt(self, encrypted_data):
        fernet = Fernet(self.encryption_key)
        decrypted_data = fernet.decrypt(encrypted_data)
        return decrypted_data.decode()
    
