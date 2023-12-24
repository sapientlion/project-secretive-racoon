# Project "Secretive Racoon"

Project "Secretive Racoon" is a simple TUI program for encrypting and decrypting data using AES encryption algorithm.
This project is not intended to be used in production environments and its sole purpose is to demonstrate one of the
ways to implement interfacing between the library (i.e. pycryptodome) and user. The project is work-in-progress and will 
remain so indefinitely. As such, expect bugs and inconsistencies.

## :wrench: How to Use :wrench:

The easiest way to run the project is to use PyCharm. From there, navigate to the main file, called "__init__.py", and
click on "Run". Follow the instructions given on the screen.

Do mind that, after the data has been successfully encrypted by the program, it will output a keyring with which you'll 
be able to decrypt the file containing the aforementioned data. Write it down somewhere, or otherwise you won't be able 
to get access to the contents of encrypted file.

## :exclamation: Known Issues :exclamation:

* Some keys may contain spaces or null characters. That may cause a problem where program refuses to accept the key due
to the missing characters, especially at the end of a key. For the sake of simplicity, re-encrypt the file and try
to decrypt it using the newly supplied key.

## :coffee: A Cup of Coffee & Stuff :coffee:

You can buy me a cup of coffee at https://ko-fi.com/sapientlion.

## :scroll: License :scroll:

Project "Secretive Racoon" is released under the MIT License. Please read LICENSE file for further details regarding the 
license.
