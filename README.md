# Image Encryption Tool

This project is a Python-based tool that encrypts and decrypts images using pixel manipulation. It was developed as part of my cybersecurity internship at Prodigy Infotech.

## Features
- **Encryption**: Applies a mathematical transformation to image pixels for confidentiality.
- **Decryption**: Reverses the transformation to retrieve the original image.
- **Customizable Key**: Users can specify an integer key for encryption and decryption.

## Technologies Used
- **Python**: Programming language used for implementation.
- **Pillow**: Library for image processing.

## Prerequisites
- Python 3.x installed.
- Install the Pillow library using:
  ```bash
  pip install pillow

## How to Use

Follow these steps to use the Image Encryption Tool:

1. **Clone the Repository**:
   Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/tholumuzikhuboni/PRODIGY_CY_02.git

2. **Navigate to the Project Directory**:
   Move into the project's directory
   ```bash
   cd image-encryption-tool

3. **Install Dependencies**:
   Make sure Python 3.x is installed. Then, install the required library using:
   ```bash 
   pip install pillow

4. **Run the Script**:
   Start the tool by executing:
   ```bash 
   python image_encryptor.py

5. **Encrypt an Image**:
   - Choose the "Encrypt an Image" option in the menu.
   - Provide the following inputs:
     - **Path to the input image**: The location of the image you want to encrypt (e.g., `images/input.jpg`).
     - **Path to save the encrypted image**: The location where the encrypted image should be saved (e.g., `images/encrypted_image.jpg`).
     - **Encryption key**: An integer key for encryption (e.g., `42`).

6. **Decrypt an Image**:
   - Choose the "Decrypt an Image" option in the menu.
   - Provide the following inputs:
     - **Path to the encrypted image**: The location of the previously encrypted image (e.g., `images/encrypted_image.jpg`).
     - **Path to save the decrypted image**: The location where the decrypted image should be saved (e.g., `images/decrypted_image.jpg`).
     - **Decryption key**: The same integer key used during encryption (e.g., `42`).



