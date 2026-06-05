import os
import hashlib
import time

def calculate_file_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except:
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

print("[*] تم تشغيل نظام مراقبة الملفات بنجاح...")
