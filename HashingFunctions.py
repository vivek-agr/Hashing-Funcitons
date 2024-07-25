import hashlib
# Import getpass for secure password input (optional)
# import getpass

def generate_hash(data, algorithm):
  """
  Generates a hash value for the provided data using the specified algorithm.

  Args:
      data: The data to hash (string).
      algorithm: The hashing algorithm to use (e.g., "md5", "sha256").

  Returns:
      The generated hash value (string).
  """
  # Convert data to bytes for hashing
  data_bytes = data.encode()
  
  # Get the appropriate hash function object
  hash_function = getattr(hashlib, algorithm)()
  
  # Update the hash function with the data
  hash_function.update(data_bytes)
  
  # Return the hashed data in hexadecimal format
  return hash_function.hexdigest()

# Uncomment this block if using getpass
# data = getpass.getpass("Enter data to hash: ")

# Example usage with user input (uncomment the following line if desired)
# data = input("Enter data to hash: ")

# Example usage with predefined string
data = "This is some data to hash!"

# Generate MD5 hash
md5_hash = generate_hash(data, "md5")
print(f"MD5 Hash: {md5_hash}")

# Generate SHA-256 hash
sha256_hash = generate_hash(data, "sha256")
print(f"SHA-256 Hash: {sha256_hash}")