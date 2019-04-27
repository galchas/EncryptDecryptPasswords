import os
from cryptography.fernet import Fernet
from os.path import expanduser


class Encryption:

    def __init__(self, password, username, output_path='', create_new_key=False):
        self.password = password
        self.username = username
        self.output_path = os.path.join(output_path, 'alpbate_bytes.bin')
        self.key = self._save_new_key() if create_new_key is True else self._get_key()

    def encrypt(self):
        cipher_suite = Fernet(self.key)
        ciphered_text = cipher_suite.encrypt(self.password)
        with open(self.output_path, 'wb') as file_object:
            file_object.write(ciphered_text)

    def decrypt(self):
        cipher_suite = Fernet(self.key)
        with open(self.output_path, 'rb') as file_object:
            for line in file_object:
                encryptedpwd = line
            uncipher_text = (cipher_suite.decrypt(encryptedpwd))
            plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8")  # convert to string
        return plain_text_encryptedpassword

    def _get_key(self):
        key_file_name = 'id_key'
        key = str()
        key_path = os.path.join(expanduser("~"), '.ssh')
        with open(os.path.join(key_path, key_file_name), 'rb') as file_object:
            for line in file_object:
                key = line
        return key

    def _save_new_key(self):
        key = Fernet.generate_key()
        key_file_name = 'id_key'
        key_path = os.path.join(expanduser("~"), '.ssh')
        if not os.path.exists(key_path):
            os.makedirs(key_path)
        with open(os.path.join(key_path, key_file_name), 'wb') as file_object:
            file_object.write(key)
        return key


if __name__ == '__main__':
    demo = Encryption('joliata11', '','',True)
    demo.encrypt()
    demo = Encryption('joliata11', '', '')
    print demo.decrypt()
