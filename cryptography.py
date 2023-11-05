# IMPORTS
from tabulate import tabulate
import string
import sys, getopt

# python cryptography.py -m "I know you well" -k 7 -t True -l True encrypt

OPTS, ARGS = getopt.getopt(sys.argv[1:], 'k:m:c:t:i:l:a:', ['key', 'message', 'ciphertext', 'tabulate', 'interactive', 'label', 'algorithm'])

# GLOBALS
NUMBERS = list(range(26))
ALPHABETS = string.ascii_uppercase
ALPHABETS_NUMS_DICT = {alpha: num for num, alpha in zip(NUMBERS, ALPHABETS)}
NUMS_ALPHABETS_DICT = {num: alpha for num, alpha in zip(NUMBERS, ALPHABETS)}
MESSAGE = None
CIPHER = None
PLAINTEXT = None
IS_TABULATED = False
KEY = 0
IS_INTERACTIVE = False
IS_LABELED = False
ENCRYPTION_ALGORITHM = None

def encrypt_ceasercipher(message: str, key: str):
        key = int(key);      # validation
        # take only the alphabets and make the message in upper case.
        message = [letter.upper() for letter in message if letter.isalpha()]
        message_length = len(message)
        # generate corresponding numbers for the message
        message_nums = [ALPHABETS_NUMS_DICT[letter] for letter in message]

        # generate key numbers: [key] * message length
        key_nums = [key] * message_length
        sums = [message_num+key_num for message_num, key_num in zip(message_nums, key_nums)]
        cipher_nums = [sum_num%26 for sum_num in sums]
        cipher_text = [NUMS_ALPHABETS_DICT[num] for num in cipher_nums]
             
        if IS_TABULATED:
            if IS_LABELED:
                message.insert(0, 'Message'); message_nums.insert(0, 'N-Value'); key_nums.insert(0, 'K-Value')
                sums.insert(0, 'Sum(+)'); cipher_nums.insert(0, 'Mod26'), cipher_text.insert(0, 'Cipher')
            data = [message, message_nums, key_nums, sums, cipher_nums, cipher_text]
            return tabulate(data, '', 'fancy_grid')
        else:
            cipher_text = ''.join(cipher_text)
            return cipher_text


def encrypt_viginerecipher(message: str, key: str):
        # take only the alphabets and make the message in upper case.
        message = [letter.upper() for letter in message if letter.isalpha()]
        message_length = len(message)
        # generate corresponding numbers for the message
        message_nums = [ALPHABETS_NUMS_DICT[letter] for letter in message]

        # generate key numbers: [key] * message length
        key = [k.upper() for k in key if key.isalpha()]
        keys_list = []
        key_length = len(key)
        i = 0
        while i != message_length:
            keys_list.append(key[i%key_length])
            i+=1
        key_nums = [ALPHABETS_NUMS_DICT[k] for k in keys_list]
        sums = [message_num+key_num for message_num, key_num in zip(message_nums, key_nums)]
        cipher_nums = [sum_num%26 for sum_num in sums]
        cipher_text = [NUMS_ALPHABETS_DICT[num] for num in cipher_nums]
             
        if IS_TABULATED:
            if IS_LABELED:
                message.insert(0, 'Message'); message_nums.insert(0, 'N-Value'); key_nums.insert(0, 'K-Value')
                sums.insert(0, 'Sum(+)'); cipher_nums.insert(0, 'Mod26'), cipher_text.insert(0, 'Cipher')
                keys_list.insert(0, 'Key')
            data = [message, message_nums, keys_list, key_nums, sums, cipher_nums, cipher_text]
            return tabulate(data, '', 'fancy_grid')
        else:
            cipher_text = ''.join(cipher_text)
            return cipher_text
        
def decrypt_ceasercipher(cipher: str, key: str):
        key = int(key);      # validation
        # take only the alphabets and make the message in upper case.
        cipher = [letter.upper() for letter in cipher if letter.isalpha()]
        message_length = len(cipher)
        # generate corresponding numbers for the message
        message_nums = [ALPHABETS_NUMS_DICT[letter] for letter in cipher]

        # generate key numbers: [key] * message length
        key_nums = [key] * message_length
        diff = [message_num-key_num for message_num, key_num in zip(message_nums, key_nums)]
        cipher_nums = [sum_num%26 for sum_num in diff]
        cipher_text = [NUMS_ALPHABETS_DICT[num] for num in cipher_nums]
             
        if IS_TABULATED:
            if IS_LABELED:
                cipher.insert(0, 'Message'); message_nums.insert(0, 'N-Value'); key_nums.insert(0, 'K-Value')
                diff.insert(0, 'Diff(-)'); cipher_nums.insert(0, 'Mod26'), cipher_text.insert(0, 'Cipher')
            data = [cipher, message_nums, key_nums, diff, cipher_nums, cipher_text]
            return tabulate(data, '', 'fancy_grid')
        else:
            cipher_text = ''.join(cipher_text)
            return cipher_text
        

def decrypt_viginerecipher(cipher: str, key: str):
        # take only the alphabets and make the message in upper case.
        cipher = [letter.upper() for letter in cipher if letter.isalpha()]
        message_length = len(cipher)
        # generate corresponding numbers for the message
        message_nums = [ALPHABETS_NUMS_DICT[letter] for letter in cipher]

        # generate key numbers: [key] * message length
        key = [k.upper() for k in key if key.isalpha()]
        keys_list = []
        key_length = len(key)
        i = 0
        while i != message_length:
            keys_list.append(key[i%key_length])
            i+=1
        key_nums = [ALPHABETS_NUMS_DICT[k] for k in keys_list]
        diff = [message_num-key_num for message_num, key_num in zip(message_nums, key_nums)]
        cipher_nums = [sum_num%26 for sum_num in diff]
        cipher_text = [NUMS_ALPHABETS_DICT[num] for num in cipher_nums]
             
        if IS_TABULATED:
            if IS_LABELED:
                cipher.insert(0, 'Message'); message_nums.insert(0, 'N-Value')
                key_nums.insert(0, 'K-Value'); diff.insert(0, 'Diff(-)')
                cipher_nums.insert(0, 'Mod26'); cipher_text.insert(0, 'Cipher')
                keys_list.insert(0, 'Key')
            data = [cipher, message_nums, keys_list, key_nums, diff, cipher_nums, cipher_text]
            return tabulate(data, '', 'fancy_grid')
        else:
            cipher_text = ''.join(cipher_text)
            return cipher_text
        

# SETTING ARGUMENTS
for key, value in OPTS:
    if key == '-m':
        MESSAGE = value
    if key == '-k':
        KEY = value
    if key == '-c':
        CIPHER = value
    if key == '-t':
         IS_TABULATED = bool(value)
    if key == '-i':
         IS_INTERACTIVE = bool(value)
    if key == '-l':
         IS_LABELED = bool(value)
    if key == '-a':
         ENCRYPTION_ALGORITHM = value


if ARGS[-1].lower() == 'encrypt':
    if IS_INTERACTIVE:
        ENCRYPTION_ALGORITHM = input("ENCRYPTION ALGORITHM: ")
        MESSAGE = input("ENTER A MESSAGE [STRING]: ")
        KEY = int(input("ENTER A KEY [INTEGER]: "))
        IS_TABULATED = bool(input("DO U WANNA TABULATE RESULTS [True/False]: "))
        IS_LABELED = bool(input("DO U WANNA LABEL YOUR TABLE: [True/False]: "))
    if ENCRYPTION_ALGORITHM.lower() == 'ceaser':
        ciphertext = encrypt_ceasercipher(MESSAGE, KEY)
        print(ciphertext)
    elif ENCRYPTION_ALGORITHM.lower() == 'viginere':
        ciphertext = encrypt_viginerecipher(MESSAGE, KEY)
        print(ciphertext)

elif ARGS[-1].lower() == 'decrypt':
    if IS_INTERACTIVE:
        ENCRYPTION_ALGORITHM = input("ENCRYPTION ALGORITHM: ")
        MESSAGE = input("ENTER A MESSAGE [STRING]: ")
        KEY = int(input("ENTER A KEY [INTEGER]: "))
        IS_TABULATED = bool(input("DO U WANNA TABULATE RESULTS [True/False]: "))
        IS_LABELED = bool(input("DO U WANNA LABEL YOUR TABLE: [True/False]: "))
    if ENCRYPTION_ALGORITHM.lower() == 'ceaser':
        plaintext = decrypt_ceasercipher(CIPHER, KEY)
        print(plaintext)
    elif ENCRYPTION_ALGORITHM.lower() == 'viginere':
        plaintext = decrypt_viginerecipher(CIPHER, KEY)
        print(plaintext)