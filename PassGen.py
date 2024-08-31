import secrets
import string

def generate_password(length):
    # Define the full pool of characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Select at least one character from each character type for complexity
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices from the full pool
    password += [secrets.choice(characters) for _ in range(length - 4)]

    # Shuffle the resulting password to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        password_length = int(input("Enter the length of each password: "))
        
        if num_passwords <= 0 or password_length <= 0:
            print("Please enter positive values for number of passwords and password length.")
            return

        passwords = [generate_password(password_length) for _ in range(num_passwords)]

        print("\nGenerated Passwords:")
        for password in passwords:
            print(password)

    except ValueError as e:
        print("Please enter valid integer values.")

if __name__ == "__main__":
    main()
