def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def get_valid_shift():
    while True:
        try:
            return int(input("Enter shift value (e.g., 3): "))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()

    if choice not in ('e', 'd'):
        print("Invalid choice. Please type 'e' or 'd'.")
        return

    message = input("Enter your message: ")
    shift = get_valid_shift()

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print("🔐 Encrypted message:", encrypted)
    else:
        decrypted = caesar_decrypt(message, shift)
        print("🔓 Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
