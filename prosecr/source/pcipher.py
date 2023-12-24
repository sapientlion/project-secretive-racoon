from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from os.path import exists


class PCipher:
    """
    Custom-made cipher which uses AES encryption algorithm as a basis for all encryption and decryption processes.
    """

    _data = bytes()                 # Raw data or decrypted data.
    _cipher_text = bytes()          # Encrypted data.
    _authentication_tag = bytes()   # An authentication tag.
    key = str('')                   # A decryption key.
    nonce = str('')                 # A unique initialization vector which must be used once.

    def encrypt(self, key_length: int(), data):
        """
        Encrypt given data using AES algorithm
        :param key_length: key length
        :param data: data to encrypt
        :return: encrypted data as a series of bytes
        """

        if data is not None:
            self._data = data

        #
        # Class attribute must not be empty.
        #
        if not self._data:
            return None

        #
        # Generate a pseudo-random key.
        #
        self.key = get_random_bytes(key_length)
        #
        # Initialize a new cipher using newly generated key.
        #
        cipher = AES.new(self.key, AES.MODE_EAX)
        #
        # Encrypt data.
        #
        self._data, self._authentication_tag = cipher.encrypt_and_digest(self._data)
        #self._cipher_text, self._authentication_tag = cipher.encrypt_and_digest(self._data)
        self.nonce = cipher.nonce

        return self._data
        #return self._cipher_text

    def decrypt(self, key):
        """
        Decrypt preceding encrypted data
        :param key: preceding key for unlocking data
        :return: decrypted data as a series of bytes
        """

        if key != '':
            self.key = key

        #
        # Class attributes must not be empty.
        #
        if self.key == '':
            return ''

        #
        # Initialize a new cipher using a key and a nonce.
        #
        cipher = AES.new(self.key, AES.MODE_EAX, self.nonce)
        #
        # Decrypt data.
        #
        self._data = cipher.decrypt_and_verify(self._data, self._authentication_tag)
        #self._data = cipher.decrypt_and_verify(self._cipher_text, self._authentication_tag)

        return self._data
