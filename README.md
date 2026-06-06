File Integrity Monitor (FIM) using Python
Project Overview
This is a lightweight File Integrity Monitor (FIM) built from scratch using Python. It continuously monitors a target directory for any unauthorized modifications, creations, or deletions of files. This project applies the Integrity pillar of the CIA Triad in cybersecurity.
Cybersecurity Concepts Applied
 Cryptography & Hashing: Utilizes the SHA-256 algorithm to generate secure digital fingerprints (hashes) for baseline validation.
 Baseline Security: Establishes a secure "known-good" baseline state to compare future modifications against.
 Continuous Monitoring: Real-time automated detection of file integrity anomalies (Blue Teaming / Security Automation).
How it Works
1 Baseline Creation: The script scans the target directory and records the SHA-256 hash of each file.
2 Real-time Detection: It regularly refetches the hashes and alerts the user if:
 A file's hash has changed (Modified).
 A file is missing (Deleted).
 A new untrusted file appears (Created/Injected).
How to Run
1 Clone the repository.
2 Run the script using terminal:
python3 fim.py
Disclaimer: This tool was developed for educational and ethical purposes only.



‫ # File Integrity Monitor (FIM) & Encryption Toolkit

File Integrity Monitor (FIM) using Python Project Overview: This is a lightweight File Integrity Monitor (FIM) built from scratch using Python. It continuously monitors a target directory for any unauthorized modifications, creations, or deletions of files. This project applies the Integrity pillar of the CIA Triad in cybersecurity. Applied Cryptography & Hashing: Utilizes the SHA-256 algorithm to generate secure digital fingerprints (hashes) for baseline validation.

## 🛠 Features & Tools:
- **FIM:** Real-time automated detection of file integrity anomalies.
- **Encryption:** Secure encryption and decryption tools for sensitive files using `secret.key`.

## 🚀 How to Use:
1. **For Monitoring:**
   `python3 fim.py`
2. **To Encrypt a file:**
   `python3 encrypt.py`
3. **To Decrypt a file:**
   `python3 decrypt.py`

---
*Disclaimer: This tool was developed for educational and ethical purposes only.*
