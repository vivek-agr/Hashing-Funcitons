1. Importing Libraries:

We'll use the hashlib library for hashing functions and potentially getpass for secure user input (optional).

2. Hashing Function:

Define a function that takes the data (as a string) and the hashing algorithm (MD5 or SHA-256) as arguments (generate_hash)

3. User Input (Optional):

You can prompt the user to enter the data they want to hash

4. Program Flow:

Call the generate_hash function with the user input (or a predefined string) and the desired algorithm (MD5 or SHA-256).
Print the generated hash value.


Explanation:

The generate_hash function takes the data and algorithm as input.
It converts the data to bytes as hashing functions typically work with binary data.
It retrieves the corresponding hash function object using getattr based on the algorithm argument (e.g., hashlib.md5() for MD5).
It updates the hash function with the data bytes.
Finally, it returns the hashed data in hexadecimal format using hexdigest().

This code demonstrates how to generate MD5 and SHA-256 hashes for a given string. You can experiment with different data and hashing algorithms provided by the hashlib library. Remember, MD5 is not considered secure for many applications due to its vulnerability to collisions. SHA-256 is a more robust option for most use cases.