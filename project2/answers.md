# Part 1
## 1.1 
1. PBKDF2 (Password-based key derivation function 2) is a cryptographic algorithm used to deter brute force attacks. It does so by forcing the computer to calculate a huge number of iterations on the hash, making the process intentionally slow. Hackers trying to brute force this algorithm will be faced with a significant delay on each attack, making the process almost impossible. 
2. Human made passwords are relatively weak and are usually crackable using brute force methods and this algorithm prevents that.

## 1.2 
1. The checksums are different because the openssl "salted" the password during encryption by adding random characters to the string. This means that the same password will probably never produce the same hash twice. 
2. Without salt, hackers that steal password hashes could use a table of common passwords and their respective hashes to reverse engineer matching hashes.

## 1.3 
1. The encryption produced 5 distinct blocks, the most common block appeared 27 times in the output. 
2. ECB mode leaks patterns in the plaintext because identical plaintext blocks are encrypted into identical ciphertext blocks. This means that if there are repeating patterns in the data being encrypted, those patterns will be visible in the ciphertext. Information can stil be inferred such as data structure, frequency of blocks, and possibly the type of data. For example an image will still look similar but distorted because the same colors will produce the same ciphertext. 
3. Before assuming that AES is secure I would ask if the correct mode is used and to see ouputs from various data types to spot blocks and repition.

# Part 2

## 2.2
1. The SHA-256 hash does not protect my collegue becuase if an attacker is able to intercept the file, they can modify the file and then compute a new SHA-256 hash to send. When my colleague rehashes to verify, it checks out even though the contents are altered. 
2. An HMAC combines the hash with a secret key, so if the attacker wanted to modify the contents of the message, they would need to know the secret key to generate a new hash. Since only me and my colleague know the secret, the hash is safe. 
3. In SHA256, the attacker can modify the file and go undetected becuase they can also alter the hash. In the HMAC case, the attacker can modify the file, but my colleague can detect the change, and will not execute or trust the file, keeping them safe.

# Part 3

## 3.3
1. This check proves that you actually own the email address ascosiated with the uploaded key. It doesn't prove that I am actually me, or that the key belongs to me because others could have access to my account. 
2. The only real way to verify that the key belongs to the classmate is to meet them in person and have them physically give you the fingerprint. Otherwise there is no way to be 100% sure. If you can only use the network to communicate, you could use a trusted authority like a certificate autority that is very difficult to spoof or hack. You could also have them video call and show the fingerprint.

# Part 4
## 4.2
1. The pubkey enc packet contains 4092 bits and is used to encrypt a symmetric key. The encrypted data packet contains the actual message, which is encrypted using the symmetric key. 
2. Encrypting the entire message with RSA would be impossible for large messages becuase RSA has size limits depending on the key size. RSA is also very slow because it uses exponentiaion and modular algos. Instead, GPG creates a symetric key using AES with some key, encrypts that key with RSA since its small, and then sends both the encrypted key and message.
3. Hybrid Approach. 

## 4.3
1. private key for signing,
2. public to verify, 
3. public for encryption
4. private for decryption. 
5. Signing gives you the ability to verify the authenticity of the sender and guarentees that the message was not altered (integrity + authentication). Encryption only provide confidentiality.

# Part 5

The eliptic curve algorithm used in Ed25519 is smaller because it is more secure per bit than RSA. This is because breaking ECC requires solving the elliptic curve discrete log problem, which is harder than factoring large numbers.

## 7.2 Code Review

### Problems with the code and CIA violation:
1. The private key is printed to the console, which may track history. This means if an attacker gains access to the console history, they would be able to decrypt all files that were encoded and steal the information. Confidentiality.
2. The key length is not validated, so any key that is not 32 bytes as required for AES256 will be accepted. If the module accepts them its a major security flaw becuase passing a shorter key weakens the encryption, but the docs guarentee AES256. If they are rejected, the script has no error handling so the entire program will fail. Availability.
3. It tries to encrypt the entire file at the same time. Encrypting a large file like a video or database will crash the program or crypto module because it will exhaust RAM. Attackers could intentially upload large files to DDoS the server. The program should buffer the file in chunks and enrypt. Integrity.
4. No metadata is stored about the file so it can be swapped or renamed without detection. Integrity.

## 7.3 Fixes
1. Added key validiation to ensure the key is 32 bytes long. If not, a ValueError is raised.
2. Removed the print statement that outputs the key to the console to prevent accidental exposure of the key. Used boto to securely store the key in AWS Secrets Manager instead.
3. Added chunked reading and writing of the file to prevent memory exhaustion when encrypting large files. The file is read and encrypted in 64KB chunks, and the nonce is prepended to the output file only once at the beginning.