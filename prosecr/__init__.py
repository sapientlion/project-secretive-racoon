from prosecr.source.pcipher import PCipher

if __name__ == "__main__":
    loop_flag = True
    #pcipher = PCipher()

    while loop_flag:
        print('(1) Encrypt\n')
        print('(2) Decrypt\n')
        print('(3) Exit\n\n')

        file_flag = True
        value = int(input('PSR: '))

        match value:
            #
            # Encrypt data and write it to the file.
            #
            case 1:
                '''path = input('File path: ')
                file_data = pcipher.read(path)

                if file_data is None:
                    file_flag = False

                    print('PSR: failed to read the file. Try again.\n')
                else:
                    file_flag = True
                    encrypted_data = pcipher.encrypt(16, file_data)

                    pcipher.write(path)

                    print('PSR: file is encrypted and ready to be decrypted.\n')'''
            #
            # Load encrypted data into the program and decrypt it.
            #
            case 2:
                '''path = input('File path: ')

                if file_flag is False:
                    print('PSR: failed to decrypt the file. Encrypt the data first and then decrypt it.\n')
                else:
                    decrypted_data = pcipher.decrypt(pcipher.key)

                    pcipher.write(path)
                    print('PSR: file is decrypted.\n')'''
            case 3:
                loop = False

                break
            case default:
                print('Unrecognized command. Try again.')
