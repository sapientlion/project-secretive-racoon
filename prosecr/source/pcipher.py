from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class PCipher:
    """
    Custom-made cipher which uses AES encryption algorithm as a basis for all encryption and decryption processes.
    """

    _data: bytes = bytes()                   # Raw data or decrypted data.
    _authentication_tag: bytes = bytes()     # An authentication tag.
    _nonce: bytes = bytes()                 # A unique initialization vector which must be used once.
    _key: bytes = bytes()                   # A decryption key.

    def get_data(self):
        return self._data

    def get_nonce(self):
        return self._nonce

    def get_key(self):
        return self._key

    def get_tag(self):
        return self._authentication_tag

    def encrypt(self, key_length: int, data: bytes):
        """
        Encrypt given data using AES algorithm
        :param key_length: key length
        :param data: data to encrypt
        :return: encrypted data as a series of bytes
        """

        if data is not None:
            self._data = data

        if not self._data:
            return None

        #
        # Generate a pseudo-random key.
        #
        self._key = get_random_bytes(key_length)
        #
        # Initialize a new cipher using newly generated key.
        #
        cipher = AES.new(self._key, AES.MODE_EAX)
        #
        # Encrypt data.
        #
        self._data, self._authentication_tag = cipher.encrypt_and_digest(self._data)
        self._nonce = cipher.nonce

        return self

    def decrypt(self, nonce: bytes, key: bytes, authentication_tag: bytes, data: bytes, ):
        """
        Decrypt preceding encrypted data
        :param key: preceding key for getting access to the data
        :return: decrypted data as a series of bytes
        """

        if nonce is not None:
            self._nonce = nonce

        if nonce is None:
            return None

        if key is not None:
            self._key = key

        if self._key is None:
            return None

        if authentication_tag is not None:
            self._authentication_tag = authentication_tag

        if not self._authentication_tag:
            return None

        if data is not None:
            self._data = data

        if not self._data:
            return None

        #
        # Initialize a new cipher using a key and a nonce.
        #
        cipher = AES.new(self._key, AES.MODE_EAX, self._nonce)
        #
        # Decrypt data.
        #
        self._data = cipher.decrypt_and_verify(self._data, self._authentication_tag)

        return self
