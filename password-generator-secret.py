import re
import secrets
import string


class PasswordGenerationError(Exception):
    """Custom exception for password generation errors."""
    pass


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generates a secure password with specified constraints.

    Parameters:
    length (int): Total length of the password.
    nums (int): Minimum number of numeric characters.
    special_chars (int): Minimum number of special characters.
    uppercase (int): Minimum number of uppercase letters.
    lowercase (int): Minimum number of lowercase letters.

    Returns:
    str: The generated password.

    Raises:
    PasswordGenerationError: If constraints cannot be met.
    """
    # Define the character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_characters = letters + digits + symbols

    # Validate input
    if any(param < 0 for param in [nums, special_chars, uppercase, lowercase, length]):
        raise PasswordGenerationError("All parameters must be non-negative integers.")

    if length < nums + special_chars + uppercase + lowercase:
        raise PasswordGenerationError(
            "Password length is too short to meet the constraints."
        )

    while True:
        password = ''.join(secrets.choice(all_characters) for _ in range(length))

        # Define constraints and their corresponding patterns
        constraints = [
            (nums, r'\d'),  # Digits
            (special_chars, fr'[{symbols}]'),  # Special characters
            (uppercase, r'[A-Z]'),  # Uppercase letters
            (lowercase, r'[a-z]')  # Lowercase letters
        ]

        # Check if all constraints are met
        if all(
                len(re.findall(pattern, password)) >= constraint
                for constraint, pattern in constraints
        ):
            break

    return password


if __name__ == "__main__":
    print("Secure Password Generator")
    try:
        password = generate_password(length=16, nums=2, special_chars=2, uppercase=2, lowercase=2)
        print("Generated password:", password)
    except PasswordGenerationError as e:
        print("Error:", e)
