# Intro to cryptography

# How cryptography *can work* - ROT13
Introduce the idea of ROT13
- **Hello World** --> **Uryyb Jbeyq** --> **Hello World**
- https://en.wikipedia.org/wiki/ROT13
- simple-ish to program because 13 + 13 = 26 --> 26 letters

Introduct the ASCII table http://www.asciitable.com/
- highlight the fact that letters are numbers
- Using interactive mode, show the **ord()** and **chr()** commands

Start building **rot13.py**
- Manually walk through converting **abc** --> **97 98 99** --> **110 111 112** --> **nop**
- Use a for loop to access each letter individually. *Another way to use a for loop*
- easy to start, but highlight issues as they occur
- for ease, force everythign to be lower case
- Figure out how to deal with non-letters (such as spaces)
- make encrypt/decrypt process a function

If time allows, use **base64.py** as example of more complex processing

# WARNING - Dont create your own encryption scheme!
rot13 is simple to understand, and can be easily expanded to rotx.py or encrypting files
Unless you are a full time security researcher, dont "roll-your-own" encryption scheme,
use the predefined encryption modules. What is hard for you, coudl be easy for someone else.

The goal of cryptography is that the crypto process should be commonly known. What should
be secret is the encryption keys. That way everyone can provide input on the best scheme 
to use, resulting in a better and more secure encryption process

# Legit cryptography
Highlight https://pypi.org/ as a repository of Python packages/libraris/dlls
There are 2 programs, **pip** and **pip3**. In general pip3 is for Python3
NOTE: For the cryptography library, you may need to use one of the following commands to install the cryptography module:
```
pip3 install cryptography
```
Fernet is a type of *symmetric cryptography* - same key to encrypt and decrypt
Unlike ROT13, there are different processes to encrypt and decrypt

## start in interactive mode
### generate key
```
from cryptography.fernet import Fernet
Fernet.generate_key()
```
Note the case sensitivity and the **b** before the output
The **b** refers to bytes, this is easier for the computer to handle. 
Do a `print(type(key))`  and `print(type(key.decode()))` to confirm
to remove the **b**, we **decode** it
```
key = Fernet.generate_key()  # store in a secure location
print("Key:", key.decode())
```
### encrypt data
```
plainText = "Hello There"
plainText = plainText.encode()
cipherText = Fernet(key).encrypt(plainText)
cipherText = cipherText.decode()
print(cipherText)
```
### decrypt data
```
cipherText = cipherText.encode()
key = key.encode()
plainText = Fernet(key).decrypt(cipherText)
plainText = plainText.decode()
```






# Lots of encryption examples online
https://cryptography.io/en/latest/fernet.html
https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/
https://devqa.io/encrypt-decrypt-data-python/
https://www.programcreek.com/python/example/98805/cryptography.fernet.Fernet
https://docs.python-guide.org/scenarios/crypto/

