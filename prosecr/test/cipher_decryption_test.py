import unittest

from prosecr.source.pciphersimplified import PCipherSimplified


class PCipherDecryption(unittest.TestCase):
    __message = 'Hello, World!'
    __message_encrypted = None
    __key_length = 16
    __cipher = PCipherSimplified()

    def test_different_message(self):
        __message_encrypted = self.__cipher.encrypt(self.__key_length, 'Nah, i`ll pass this time.')
        __message_decrypted = self.__cipher.decrypt(self.__cipher.key)

        self.assertNotEqual(str(__message_decrypted, 'utf-8'), self.__message)

    def test_decryption_is_successful(self):
        __message_encrypted = self.__cipher.encrypt(self.__key_length, self.__message)
        __message_decrypted = self.__cipher.decrypt(self.__cipher.key)

        self.assertEqual(str(__message_decrypted, 'utf-8'), self.__message)


if __name__ == '__main__':
    unittest.main()
