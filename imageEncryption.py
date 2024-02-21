# Import the Image module from PIL
from PIL import Image

# Define a function to encrypt an image with a key
def encrypt_image(image_path, key):
    # Open the image and convert it to RGB mode
    image = Image.open(image_path).convert("RGB")
    # Get the width and height of the image
    width, height = image.size
    # Convert the image to a byte array
    image_data = bytearray(image.tobytes())
    # Convert the key to a byte string
    key = key.encode()
    # Initialize an empty byte array for the encrypted image data
    encrypted_image_data = bytearray()
    # Loop through each byte of the image data
    for i in range(len(image_data)):
        # XOR the byte with the corresponding byte of the key
        # If the key is shorter than the image data, use modulo to wrap around
        encrypted_image_data.append(image_data[i] ^ key[i % len(key)])
    # Create a new image from the encrypted image data
    encrypted_image = Image.frombytes("RGB", (width, height), bytes(encrypted_image_data))
    # Return the encrypted image
    return encrypted_image

# Define a function to decrypt an image with a key
def decrypt_image(image, key):
    # Get the width and height of the image
    width, height = image.size
    # Convert the image to a byte array
    image_data = bytearray(image.tobytes())
    # Convert the key to a byte string
    key = key.encode()
    # Initialize an empty byte array for the decrypted image data
    decrypted_image_data = bytearray()
    # Loop through each byte of the image data
    for i in range(len(image_data)):
        # XOR the byte with the corresponding byte of the key
        # If the key is shorter than the image data, use modulo to wrap around
        decrypted_image_data.append(image_data[i] ^ key[i % len(key)])
    # Create a new image from the decrypted image data
    decrypted_image = Image.frombytes("RGB", (width, height), bytes(decrypted_image_data))
    # Return the decrypted image
    return decrypted_image

# image used
image_path = "image.jpg"
key = "secret"
encrypted_image = encrypt_image(image_path, key)
encrypted_image.save("encrypted_image.jpg")
decrypted_image = decrypt_image(encrypted_image, key)
decrypted_image.save("decrypted_image.jpg")
