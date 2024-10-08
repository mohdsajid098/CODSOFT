# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sDcQ2BIuMHJMefyR217OH5wUye_dsDT-
"""

import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
    """Generates a random password of the specified length.

    Args:
        length: The desired length of the password.
        include_uppercase: Whether to include uppercase letters.
        include_lowercase: Whether to include lowercase letters.
        include_numbers: Whether to include numbers.
        include_symbols: Whether to include symbols.

    Returns:
        A randomly generated password string.
    """

    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    length = int(input("Enter the desired password length: "))

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)

    print("Generated password:", password)

if __name__ == "__main__":
    main()