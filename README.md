# Secure Data Transmission App with Hashing and Encryption

This Python program uses the Fernet module from Cryptography to generate a symmetric key and encrypt the user's message and hashlib to generate a SHA-256 hash of the message. Once a message is entered, a hash is generated and the message is encrypted. The message is then decrypted using the generated key, and the hash of the decrypted message is compared to the original hash of the input message. If the message and hash match the originals, the integrity of the message is verified. 

## Installation 

Use the package manager to install cryptography

```bash
pip install cryptography
```

## Youtube video demo
[![VgpTLrSG8qQ](https://img.youtube.com/vi/VgpTLrSG8qQ/0.jpg)](https://www.youtube.com/watch?v=VgpTLrSG8qQ)

## Confidentiality, integrity, and availability 

This program upholds the principle of confidentiality by using Fernet symmetric encryption to protect the user's message. The generated key ensures that only authorized users with the correct key can see the original message.

This program upholds the principle of integrity by using SHA-256 hashing to ensure that the user's message has not been altered. When the program verififies the decrytped message via hash comparison, the message has been unaltered. 

This program upholds the principle of availability by reliably generating a unique key and encryption for each user message and decrypting and verifying the message in real time. This means that the data is always immediately accessabile.

## Entropy and key generation

The role of entropy and key generation is handled when Fernet module generates a unique symmetric key for each entered user message, even if the same message is entered more than once. Because the key is symmetric, it must be used to decrypt the data. 
