# Define a function to encrypt a message with a key
def encrypt(message, key):
    # Convert the message and the key to byte strings
    message = message.encode()
    key = key.encode()
    # Initialize an empty byte string for the ciphertext
    ciphertext = b""
    # Loop through each byte of the message
    for i in range(len(message)):
        # XOR the byte with the corresponding byte of the key
        # If the key is shorter than the message, use modulo to wrap around
        ciphertext += bytes([message[i] ^ key[i % len(key)]])
    # Return the ciphertext as a hexadecimal string
    return ciphertext.hex()

# Define a function to decrypt a ciphertext with a key
def decrypt(ciphertext, key):
    # Convert the ciphertext and the key to byte strings
    ciphertext = bytes.fromhex(ciphertext)
    key = key.encode()
    # Initialize an empty byte string for the plaintext
    plaintext = b""
    # Loop through each byte of the ciphertext
    for i in range(len(ciphertext)):
        # XOR the byte with the corresponding byte of the key
        # If the key is shorter than the ciphertext, use modulo to wrap around
        plaintext += bytes([ciphertext[i] ^ key[i % len(key)]])
    # Return the plaintext as a decoded string
    return plaintext.decode()

# The message used
message = "The price of bag of rice should be double. Border shut this morning"
key = "secret"
ciphertext = encrypt(message, key)
print("Encrypted message:", ciphertext)
plaintext = decrypt(ciphertext, key)
print("Decrypted message:", plaintext)
