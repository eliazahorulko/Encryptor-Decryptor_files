import pyAesCrypt
import os
from posixpath import splitext

# Buffer size for pyAesCrypt
bufferSize = 512 * 1024

# Encryption function
def encryption(file, password):
    # Use the encryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        bufferSize
    )

    # Output message confirming the file encryption
    print(f"The file '{splitext(file)[0]}' has been encrypted")

    # Remove the original file
    os.remove(file)

# Function for scanning directories
def walkingByDirectories(dir, password):
    # Iterate through all files and subdirectories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # If it's a file, encrypt it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(f"Error encrypting file {path}: {ex}")
        # If it's a directory, enter it recursively
        elif os.path.isdir(path):
            walkingByDirectories(path, password)

# Get the password from the user
password = input("Enter password for encryption: ")
directory = input("Enter the directory to encrypt files in: ")
walkingByDirectories(directory, password)
