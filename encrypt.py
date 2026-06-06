from cryptography.fernet import Fernet

# 1. تحميل المفتاح السري
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# 2. تحديد اسم الملف المراد تشفيره
file_to_encrypt = "test.txt"  # يمكنك تغيير هذا الاسم لأي ملف تجربي عندك

# 3. قراءة محتوى الملف وتشفيره
with open(file_to_encrypt, "rb") as file:
    file_data = file.read()

encrypted_data = fernet.encrypt(file_data)

# 4. حفظ الملف المشفر
with open(file_to_encrypt, "wb") as file:
    file.write(encrypted_data)

print(f"تم تشفير الملف {file_to_encrypt} بنجاح!")

