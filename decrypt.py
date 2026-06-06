from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
   key = key_file.read()

fernet = Fernet(key)

with open("test.txt", "rb") as file:
   encrypted_data = file.read()

decrypted_data = fernet.decrypt(encrypted_data)

with open("test.txt", "wb") as file:
   file.write(decrypted_data)

print("تم فك التشفير بنجاح!")
