import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

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
    
    aesgcm = AESGCM(key)
    
    # Read the original file
    with open(input_file_path, "rb") as f:
        data = f.read()
    
    # Encrypt data (AESGCM automatically appends a 16-byte authentication tag to the ciphertext)
    ciphertext = aesgcm.encrypt(nonce, data, associated_data=None)
    
    # Prepend the nonce to the ciphertext so it can be retrieved during decryption
    with open(output_file_path, "wb") as f:
        f.write(nonce + ciphertext)
        
    return key


# --- Example Usage ---
if __name__ == "__main__":
    # Create a dummy file to encrypt
    with open("example.txt", "w") as f:
        f.write("Secret text message.")

    # Encrypt the file
    secret_key = encrypt_file("example.txt", "example.txt.enc")
    print(f"Encryption successful. Key (hex): {secret_key.hex()}")