# Password Generator

A Python repository showcasing different methods to generate secure passwords.

## Methods Included
1. **Using `random` Module**:
   - A simple password generator using the `random` module.
   - File: `password_generator_random.py`

2. **Using `secrets` and Regular Expressions (`re`)**:
   - A more secure password generator using `secrets` for cryptographic randomness and `re` for constraint validation.
   - File: `password_generator_secrets.py`

## Features
- Customizable password length and character constraints:
  - Minimum numbers (`nums`)
  - Minimum special characters (`special_chars`)
  - Minimum uppercase letters (`uppercase`)
  - Minimum lowercase letters (`lowercase`)
- Ensures constraints are met before returning a password.
- Implements secure random number generation with the `secrets` module.
- Clear error handling for invalid inputs.

## Usage
### Run the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/password_generator.git
