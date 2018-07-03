from cryptography.fernet import Fernet

key = Fernet.generate_key()

def encrypt(text):
    f = Fernet(key)
    encrypted = f.encrypt(text)
    data = {
        'key': key,
        'encrypted': encrypted,
    }
    return data

def decrypt(text, key):
    f = Fernet(key)
    decrypted = f.decrypt(text)
    return decrypted
