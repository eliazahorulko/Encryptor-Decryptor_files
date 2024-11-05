import pyAesCrypt
import os
from posixpath import splitext

# Buffer size for pyAesCrypt
bufferSize = 512 * 1024

# Decrypt function
def decryption(file, password):
    # Use the decryption method
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        bufferSize
    )

    # Output message confirming the file encryption
    print(f"The file '{splitext(file)[0]}' has been descrypted")

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
                decryption(path, password)
            except Exception as ex:
                print(f"Error encrypting file {path}: {ex}")
        # If it's a directory, enter it recursively
        elif os.path.isdir(path):
            walkingByDirectories(path, password)

# Get the password from the user
password = input("Enter password for decryption: ")
directory = input("Enter the directory to decrypt files in: ")
walkingByDirectories(directory, password)
