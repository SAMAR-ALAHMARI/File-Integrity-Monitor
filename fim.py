import hashlib
import os
import time
def calculate_file_hash(filepath):
sha256_hash = hashlib.sha256()
try:
with open(filepath, "rb") as f:
for byte_block in iter(lambda: f.read(4096), b""):
sha256_hash.update(byte_block)
return sha256_hash.hexdigest()
except FileNotFoundError:
return None
def create_baseline(directory_to_watch):
baseline = {}
for root, dirs, files in os.walk(directory_to_watch):
for file in files:
filepath = os.path.join(root, file)
file_hash = calculate_file_hash(filepath)
if file_hash:
baseline[filepath] = file_hash
return baseline
def monitor_directory(directory_to_watch):
print(f"[*] جاري إنشاء خط الأساس للمجلد: {directory_to_watch}")
baseline = create_baseline(directory_to_watch)
print("[+] تم إنشاء خط الأساس بنجاح. النظام الآن في وضع المراقبة المستمرة...\n")
while True:
time.sleep(3)
for filepath, registered_hash in list(baseline.items()):
if not os.path.exists(filepath):
print(f"[!!] تنبيه أمني: تم حذف الملف! -> {filepath}")
del baseline[filepath]
else:
current_hash = calculate_file_hash(filepath)
if current_hash != registered_hash:
print(f"[!!] تنبيه أمني: تم التعديل على محتوى الملف! -> {filepath}")
baseline[filepath] = current_hash
for root, dirs, files in os.walk(directory_to_watch):
for file in files:
filepath = os.path.join(root, file)
if filepath not in baseline:
current_hash = calculate_file_hash(filepath)
print(f"[!!] تنبيه أمني: تم إضافة ملف جديد غير معروف! -> {filepath}")
baseline[filepath] = current_hash
if name == "main":
target_dir = "./test_folder"
if not os.path.exists(target_dir):
os.makedirs(target_dir)
with open(os.path.join(target_dir, "safe_file.txt"), "w") as f:
f.write("This is secure data.")
monitor_directory(target_dir)
