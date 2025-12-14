# AES-256 File Encryptor & Decryptor using AES-GCM
# Requires: pip install cryptography

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

KEY_FILE = "secret.key"

# ---------- KEY MANAGEMENT ----------

def generate_key():
    # 32 bytes = 256-bit key
    key = AESGCM.generate_key(bit_length=256)
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("AES-256 key generated and saved as secret.key")


def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()


# ---------- ENCRYPTION ----------

def encrypt_file(file_path):
    key = load_key()
    aesgcm = AESGCM(key)

    with open(file_path, "rb") as f:
        data = f.read()

    # 12 bytes nonce recommended for GCM
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data, None)

    encrypted_file = file_path + ".enc"
    with open(encrypted_file, "wb") as f:
        # store nonce + ciphertext together
        f.write(nonce + ciphertext)

    print(f"Encrypted file saved as: {encrypted_file}")


# ---------- DECRYPTION ----------

def decrypt_file(file_path):
    key = load_key()
    aesgcm = AESGCM(key)

    with open(file_path, "rb") as f:
        raw = f.read()

    nonce = raw[:12]
    ciphertext = raw[12:]

    data = aesgcm.decrypt(nonce, ciphertext, None)

    if file_path.endswith(".enc"):
        decrypted_file = file_path.replace(".enc", "")
    else:
        decrypted_file = file_path + ".dec"

    with open(decrypted_file, "wb") as f:
        f.write(data)

    print(f"Decrypted file saved as: {decrypted_file}")


# ---------- MAIN ----------

if __name__ == "__main__":
    print("1. Generate AES-256 Key (run once)")
    print("2. Encrypt File")
    print("3. Decrypt File")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        path = input("Enter file path to encrypt: ")
        encrypt_file(path)
    elif choice == "3":
        path = input("Enter file path to decrypt: ")
        decrypt_file(path)
    else:
        print("Invalid choice")
