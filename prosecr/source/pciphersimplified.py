'''

MIT License

Copyright (c) 2023 Leo "SapientLion" Markoff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

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
