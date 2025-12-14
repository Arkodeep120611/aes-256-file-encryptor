# 🔐 AES-256 File Encryptor & Decryptor (Python)

A secure file encryption and decryption tool built in Python using **AES-256-GCM**.

## ✨ Features
- Encrypt any file type
- AES-256-GCM authenticated encryption
- Built-in tamper detection
- Simple command-line interface
- Secure symmetric key handling

## 🐍 Python Version
Tested with **Python 3.14**.  
Note: Some tooling may be unstable due to early ecosystem support.

## 📦 Installation
```bash
pip install -r requirements.txt
```

## 🔑 Generate Key (run once)
```bash
python encryptor.py
# choose option 1
```

This creates a `secret.key` file used for encryption and decryption.

## 🔒 Encrypt File
```bash
python encryptor.py
# choose option 2
```

## 🔓 Decrypt File
```bash
python encryptor.py
# choose option 3
```

## ⚠️ Security Warning
- If `secret.key` is lost, encrypted files **cannot be recovered**
- Do NOT share your key file
- The `.venv` directory is intentionally excluded from this repository
