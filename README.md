# RSA
Implementation of  RSA algorithm

## Overview
This is the implementation of the RSA encryption algorithm, demonstrating key generation, encryption, and decryption processes. It generates RSA public and private keys from user-provided prime numbers, encrypts plaintext messages into ciphertext using modular exponentiation, and decrypts ciphertext back into plaintext. The project also includes input validation to ensure prime number correctness and message constraints.

## Key Features
- **Prime Number Validation**: Checks if user-input primes are valid.
- **Key Generation**: Computes `n`, `φ(n)`, public exponent `e`, and private exponent `d`.
- **ASCII Support**: Encrypts/decrypts text messages character-by-character.
- **Input Validation**: Ensures the modulus `n` is large enough to handle ASCII values (≥128).

