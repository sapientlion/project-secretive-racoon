from os.path import exists

from prosecr.source.pcipher import PCipher
from prosecr.source.pcipherdata import PCipherData


def main():
    print('(1) Encrypt\n')
    print('(2) Decrypt\n')
    print('(3) Exit\n\n')

    value: int = int(input('PSR: '))

    match value:
        #
        # Encrypt data and write it to the file.
        #
        case 1:
            path: str = input('PSR: enter a path to a plain text file: ')

            if not exists(path):
                print('PSR: given path does not exist in the system. Try again.\n')

                return True

            file: PCipherData = PCipherData()

            if file.read(path) is None:
                print('PSR: failed to read the file. Try again.\n')

                return True
            else:
                pcipher: PCipher = PCipher()

                pcipher.encrypt(16, file.get_data())
                file.write(path, pcipher.get_data())

                print('PSR: file is encrypted and saved as ' + path + '.psr.\n')
                print('PSR: nonce = ' + str(pcipher.get_nonce(), 'latin')
                      + ', key = ' + str(pcipher.get_key(), 'latin')
                      + ', tag = ' + str(pcipher.get_tag(), 'latin')
                      + '\n')

                return True
        #
        # Load encrypted data into the program and decrypt it.
        #
        case 2:
            path: str = input('PSR: enter a path to a cipher text file: ')

            if not exists(path):
                print('PSR: given path does not exist in the system. Try again.\n')

                return True

            file: PCipherData = PCipherData()
            data: bytes = file.read(path)

            if data is None:
                print('PSR: failed to read the file. Try again.\n')

                return True

            nonce: str = input('PSR: enter a nonce: ')
            key: str = input('PSR: enter a key: ')
            tag: str = input('PSR: enter an authentication tag: ')
            pcipher: PCipher = PCipher()
            data: PCipher = pcipher.decrypt(
                bytes(nonce, 'latin'),
                bytes(key, 'latin'),
                bytes(tag, 'latin'),
                data)

            if data is None:
                print('PSR: failed to decrypt the file. Either nonce or key is wrong.\n')

                return True
            else:
                print(str(data.get_data().decode('latin')) + '\n')

                return True
        case 3:
            return False
        case default:
            print('Unrecognized command. Try again.')

            return True


if __name__ == "__main__":
    loop_flag: bool = True

    while loop_flag:
        loop_flag = main()
