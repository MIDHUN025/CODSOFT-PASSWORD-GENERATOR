import random
import string

def generate_password(length, use_special_chars=True, use_digits=True, use_uppercase=True):
    # Define the characters to use in the password
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length for the password: "))
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    
    # Generate the password
    password = generate_password(length, use_special_chars, use_digits, use_uppercase)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
