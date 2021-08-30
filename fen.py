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


if __name__ == "__main__":
    # write_key()
    key = load_key()
    f = Fernet(key)
    message = sys.argv[1].encode()
    print(message)
    encrypted = f.encrypt(message)
    print(encrypted)
    decrypted = f.decrypt(encrypted)
    print(decrypted)
