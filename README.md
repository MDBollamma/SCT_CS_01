# SCT_CS_01
A simple Python-based Caesar Cipher tool for encrypting and decrypting messages using a shift value. Great for beginners learning about classical cryptography and string manipulation.
# Caesar Cipher Tool 

 Caesar Cipher Tool 

A beginner-friendly Python program that implements the classic Caesar Cipher encryption and decryption technique. This tool allows users to encode or decode messages by shifting alphabetic characters while preserving non-alphabetic symbols.

 Features

- Encrypt messages with a custom shift value
- Decrypt messages using the same shift
- Handles both uppercase and lowercase letters
- Preserves punctuation, spaces, and numbers
- Input validation for shift values

 How It Works

The Caesar Cipher shifts each letter in the message by a fixed number of positions in the alphabet. For example, with a shift of 3:
- `A` becomes `D`
- `B` becomes `E`
- ...
- `Z` wraps around to `C`

Non-alphabetic characters (like spaces and punctuation) remain unchanged.

 Requirements

- Python 3.x

No external libraries are needed.

 Usage

Run the script in your terminal or Python environment:

```bash
python caesar_cipher.py


Follow the prompts:
- Choose to encrypt (e) or decrypt (d)
- Enter your message
- Provide a shift value (e.g., 3)
Example:
=== Caesar Cipher Tool ===
Type 'e' to encrypt or 'd' to decrypt: e
Enter your message: Hello, World!
Enter shift value (e.g., 3): 3
 Encrypted message: Khoor, Zruog!



