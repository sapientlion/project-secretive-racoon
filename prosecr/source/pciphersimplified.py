from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from prosecr.source.pcipher import PCipher


class PCipherSimplified(PCipher):
    def encrypt(self, key_length: int(), data):
        """
        Encrypt given string using AES algorithm
        :param key_length: key length
        :param data: data to encrypt
        :return: encrypted string as a series of bytes
        """

        if data != '':
            self._data = bytes(data, 'utf-8')

        if not self._data:
            return None

        self.key = get_random_bytes(key_length)
        cipher = AES.new(self.key, AES.MODE_EAX)
        self._cipher_text, self._data_tag = cipher.encrypt_and_digest(self._data)
        self.nonce = cipher.nonce

        return self._cipher_text
