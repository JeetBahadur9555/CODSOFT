import random
import string
def get_password_criteria():
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    return length, include_uppercase, include_numbers, include_special
def generate_password(length, include_uppercase, include_numbers, include_special):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    length, include_uppercase, include_numbers, include_special = get_password_criteria()
    password = generate_password(length, include_uppercase, include_numbers, include_special)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
