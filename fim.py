
import hashlib
import time

def calculate_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

file_to_monitor = "test.txt"
# نقرأ البصمة الأصلية
with open("baseline.txt", "r") as f:
    old_hash = f.read().strip()

print("بدأ المراقبة الآن... (اضغطي Ctrl+C للإيقاف)")

try:
    while True:
        current_hash = calculate_file_hash(file_to_monitor)
        if current_hash != old_hash:
            print("🚨 تنبيه! تم اكتشاف تغيير في الملف!")
            break
        time.sleep(2) # ينتظر ثانيتين ثم يفحص مرة أخرى
except KeyboardInterrupt:
    print("\nتم إيقاف المراقبة.")
