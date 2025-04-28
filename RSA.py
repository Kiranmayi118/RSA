import random
import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find modular inverse."""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(e, phi):
    """Find the modular inverse of e modulo phi."""
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def generate_keys(p, q):
    """Generate RSA public and private keys."""
    # Step 1: Ensure p and q are prime
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both p and q must be prime numbers.")
    
    # Step 2: Compute n = p * q
    n = p * q
    
    # Step 3: Compute Euler's totient function phi(n)
    phi = (p - 1) * (q - 1)
    
    # Step 4: Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    
    # Step 5: Compute d, the modular inverse of e modulo phi(n)
    d = modinv(e, phi)
    
    # Public key is (e, n), private key is (d, n)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    """Encrypt a message using the public key."""
    e, n = public_key
    # Convert each character to its ASCII value and encrypt
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    """Decrypt a message using the private key."""
    d, n = private_key
    # Decrypt each number to its ASCII value and convert to character
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

print("Starting RSA...")

# Get prime numbers p and q from the user
while True:
    try:
        p = int(input("Enter first prime number (p): "))
        q = int(input("Enter second prime number (q): "))
        if is_prime(p) and is_prime(q):
            break
        else:
            print("Both numbers must be prime. Please try again.")
    except ValueError:
        print("Invalid input. Please enter integers.")

# Generate keys
print(" ")
print("Generating keys...")
public_key, private_key = generate_keys(p, q)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

print(" ")
# Message to encrypt
message = input("Enter a message to encrypt: ")
print("Original Message:", message)

# Encrypt the message
print("Encrypting message...")
encrypted_message = encrypt(public_key, message)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
print("Decrypting message...")
decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted Message:", decrypted_message)

print(" ")
print("RSA completed!")