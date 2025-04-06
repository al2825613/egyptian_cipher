# Egyptian Cipher Library

This is a Python library for encrypting and decrypting text using Egyptian hieroglyphs and multiple encryption layers.

## Features:
- **Egyptian Hieroglyph Cipher:** Encrypts text into Egyptian hieroglyphic characters.
- **Base64 Cipher:** Encrypts and decrypts text using Base64 encoding.
- **Multi-Layer Encryption:** Combines Egyptian Hieroglyph and Base64 encryption.

## Installation:
You can clone or download the repository to use the library.

## Usage Example:
```python
from egyptian_cipher import multi_layer_encrypt, multi_layer_decrypt

# Encrypt text
encrypted_text = multi_layer_encrypt("Hello World 123")

# Decrypt text
decrypted_text = multi_layer_decrypt(encrypted_text)

print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
