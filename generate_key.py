from cryptography.fernet import Fernet

# إنشاء المفتاح
key = Fernet.generate_key()

# حفظ المفتاح في ملف اسمه secret.key
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("تم إنشاء المفتاح بنجاح وحفظه في ملف secret.key")

