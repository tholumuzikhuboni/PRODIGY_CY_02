from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    """Encrypt the image by modifying pixel values."""
    try:
        image = Image.open(input_path)
        encrypted_image = image.copy()
        pixels = encrypted_image.load()
        
        for i in range(image.width):
            for j in range(image.height):
                r, g, b = pixels[i, j]
                # Example transformation: add the key value (wrap around 256 for RGB values)
                pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
        
        encrypted_image.save(output_path)
        print(f"Image encrypted successfully. Saved as {output_path}")
    except Exception as e:
        print(f"Error encrypting the image: {e}")

def decrypt_image(input_path, output_path, key):
    """Decrypt the image by reversing the pixel value modification."""
    try:
        image = Image.open(input_path)
        decrypted_image = image.copy()
        pixels = decrypted_image.load()
        
        for i in range(image.width):
            for j in range(image.height):
                r, g, b = pixels[i, j]
                # Reverse transformation: subtract the key value (wrap around 256 for RGB values)
                pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
        
        decrypted_image.save(output_path)
        print(f"Image decrypted successfully. Saved as {output_path}")
    except Exception as e:
        print(f"Error decrypting the image: {e}")

def main():
    print("Image Encryption and Decryption Tool")
    print("1. Encrypt an Image")
    print("2. Decrypt an Image")
    print("3. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            input_path = input("Enter the path to the input image: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter an encryption key (integer): "))
            encrypt_image(input_path, output_path, key)
        elif choice == "2":
            input_path = input("Enter the path to the encrypted image: ")
            output_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(input_path, output_path, key)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
