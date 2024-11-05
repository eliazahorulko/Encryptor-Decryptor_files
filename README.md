Application Description for File Encryption and Decryption

This application is designed to securely encrypt and decrypt files within a specified directory, providing robust data protection by creating encrypted versions of files that can only be accessed with the correct password. The application consists of two separate modules: `encryptor.py` for encryption and `decryptor.py` for decryption.

How the Application Works

1. Encrypting Data:
   - Run the `encryptor.py` file.
   - Enter the directory path where the files you want to encrypt are located.
   - All files in the specified directory will be encrypted using a strong encryption algorithm, like AES (based on the library used).
   - After encryption, each encrypted file will be saved with a `.crp` extension, indicating it is a protected file.

2. Decrypting Data:
   - To decrypt the encrypted files, run `decryptor.py`.
   - Enter the same directory path and provide the correct password.
   - The application will decrypt all `.crp` files in the directory and restore them to their original format, making them accessible again.

Key Features

- Secure Encryption: All files are encrypted with a secure algorithm, preventing unauthorized access.
- Easy to Use: Simple command-line prompts guide users through the encryption and decryption processes.
- File Removal: After encryption, the original unencrypted files can be automatically deleted for added security.

This tool is ideal for users looking to secure sensitive files in bulk within a directory, ensuring privacy and data protection.
