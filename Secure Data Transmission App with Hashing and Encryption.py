from hashlib import sha256
from cryptography.fernet import Fernet

# Generates symmetric key
key = Fernet.generate_key()
f = Fernet(key)

# User message input
while True:
	message = input("Enter a message or press enter to quit: ")
	if message == "":
		print("The program will terminate")
		break

	# Hash user message using SHA-256
	message = message.encode()
	hash1 = sha256(message).hexdigest()

	# Encrypts user message
	encrypted_message = f.encrypt(message)
	print("Key: ", key)
	print("Encrypted message:", encrypted_message)

	# DECRYPT AND VERIFY VIA HASH COMPARISON

	# Decrypts and prints the user message using the generated key
	decrypted_message = Fernet(key).decrypt(encrypted_message)
	print("Decrypted message: ", decrypted_message.decode())

	# Hash decrypted user message
	hash2 = sha256(decrypted_message).hexdigest()

	if decrypted_message == message and hash2 == hash1:
		print("Original SHA-256 Hash:", hash1)
		print("Decrypted SHA-256 Hash: ", hash2)
		print("Integrity verified via hash comparison")
	else:
		print("Message verification failed")
