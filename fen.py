from cryptography.fernet import Fernet
from pathlib import Path
import sys

home = str(Path.home())


def write_key():
    """

    """
    key = Fernet.generate_key()

    with open(home + "/fencrypt.key", "w+b") as key_file:
        key_file.write(key)


def load_key():
    """

    """
    return open(home + "/fencrypt.key").read()


def encrypt(filename, key=load_key()):
    """
    Given a filename (str) with path included and key (bytes), it encrypts the content of the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_content = file.read()

    encrypted = f.encrypt(file_content)

    with open(filename, "wb") as file:
        file.write(encrypted)


def decrypt(filename, key=load_key()):
    f = Fernet(key)
    with open(filename, "rb") as file:
        decrypted = file.read()

    content = f.decrypt(decrypted)

    with open(filename, "wb") as file:
        file.write(content)


if __name__ == "__main__":
    # write_key()
    action = sys.argv[1]
    full_path_to_file = sys.argv[2]
    if "-d" == action:
        decrypt(full_path_to_file)
    elif "-e" == action:
        encrypt(full_path_to_file)
    else:
        print("unknown key" + action)


class Encryptor:
    """
    This class should encapsulate the logic relate to the encryption
    """
