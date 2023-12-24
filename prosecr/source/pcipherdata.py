from os.path import exists


class PCipherData:
    __data: bytes = bytes()

    def get_data(self):
        return self.__data

    def check(self, path: str):
        """
        Check whether file path exists or not in the current system.
        :param path: absolute path to a file
        :return: return False on missing file path. Otherwise, return True.
        """

        file_existence_flag = exists(path)

        if not file_existence_flag:
            return False

        return True

    def write(self, path: str, data: bytes):
        """
        Write data to a file.
        :param path: absolute path to a file.
        :param data: data to save
        :return: return None on fail. Return data on success.
        """

        if not self.check(path):
            return None

        #
        # Open the file first.
        #
        file = open(path + '.psr', 'wb')

        if file == OSError:
            return None

        if data is not None:
            self.__data = data

        if self.__data is None:
            return None

        #
        # Write data to the file.
        #
        file.write(self.__data)
        #
        # Close the file.
        #
        file.close()

        return self.__data

    def read(self, path: str):
        """
        Read data from file.
        :param path: absolute path to a file
        :return: return None on fail. Return data on success.
        """

        if not self.check(path):
            return None

        file = open(path, 'rb')

        if file == OSError:
            return None

        #
        # Read data from the file.
        #
        self.__data = file.read()

        file.close()

        return self.__data
