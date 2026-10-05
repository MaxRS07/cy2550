import os
import boto3
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

CHUNK_SIZE = 64 * 1024  # 64KB
def encrypt_file(input_file_path: str, output_file_path: str, key: bytes = None) -> bytes:
    """
    Encrypts a file using AES-256-GCM.
    
    :param input_file_path: Path to the unencrypted source file.
    :param output_file_path: Path where the encrypted file will be saved.
    :param key: Optional 32-byte AES key. If None, a cryptographically secure key is generated.
    :return: The 32-byte AES key used for encryption.
    """
    # Generate a random 256-bit (32-byte) key if one isn't provided
    if key is None:
        key = AESGCM.generate_key(bit_length=256)
    
    # AES-GCM standard requires a unique 12-byte initialization vector (nonce) for every encryption
    nonce = os.urandom(12)
    
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes long for AES-256-GCM.")
    aesgcm = AESGCM(key)
    
    # Read the original file
    with open(input_file_path, "rb") as f:
        while True:
            data = f.read(CHUNK_SIZE)
            if not data:
                break
            # Encrypt the current chunk
            ciphertext = aesgcm.encrypt(nonce, data, associated_data=None)
            with open(output_file_path, "wb") as f:
                f.write(nonce + ciphertext)
        
    return key

# --- Example Usage ---
if __name__ == "__main__":
    secrets = boto3.client("secretsmanager")

    with open("example.txt", "w") as f:
        f.write("Secret text message.")

    # Encrypt the file
    secret_key = encrypt_file("example.txt", "example.txt.enc")
    secrets.create_secret(
    Name="file-keys/example.txt.enc",
        SecretBinary=secret_key,
    )
    # wipe from memory
    del secret_key