# RSA
Implementation of  RSA algorithm

## Overview
This is the implementation of the RSA encryption algorithm, demonstrating key generation, encryption, and decryption processes. It generates RSA public and private keys from user-provided prime numbers, encrypts plaintext messages into ciphertext using modular exponentiation, and decrypts ciphertext back into plaintext. The project also includes input validation to ensure prime number correctness and message constraints.

## Key Features
- **Prime Number Validation**: Checks if user-input primes are valid.
- **Key Generation**: Computes `n`, `φ(n)`, public exponent `e`, and private exponent `d`.
- **ASCII Support**: Encrypts/decrypts text messages character-by-character.
- **Input Validation**: Ensures the modulus `n` is large enough to handle ASCII values (≥128).

## Usage
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Kiranmayi118/RSA.git
   cd RSA

2. Run the Script:
   ```bash
    python RSA.py

3. Follow the on-scree instructions to input prime numbers and a message for encryption/decryption.

## Sample Output
   ```
   Starting RSA example...
   Enter a prime number (p): 11
   Enter another prime number (q): 13
   
   Generating keys...
   Public Key (e, n): (7, 143)
   Private Key (d, n): (103, 143)
   
   Enter a message to encrypt: Hello RSA!
   Original Message: Hello RSA!
   
   Encrypting message...
   Encrypted Message: [114, 19, 76, 76, 85, 11, 128, 76, 85, 100, 33]
   
   Decrypting message...
   Decrypted Message: Hello RSA!
   
   RSA example completed!
