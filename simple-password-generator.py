import random
import string

def generate_password():
    length = int(input("Enter the password length: "))
    if length < 8:
        print("Password length should be at least 8 characters.")
        return

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    print(f"Generated password: {password}")

if __name__ == "__main__":
    generate_password()
