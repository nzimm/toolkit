#!/usr/bin/env python3
import argparse
from string import printable

def simple_encrypt(message, key):
    """ Uses key values to shift the characters in message

        Input: key <printable string> 
               message <printable string> 
        Output: encrypted_message <printable string> 
    """

    
    # generate a cypher from the key
    key_cypher = [ord(character) for character in key]
    encrypted_message = ""
    for index, character in enumerate(message):
        # Get the index of a character in message
        message_char_index = printable.index(character)

        # Calculate shift amount from the key
        index_shift = key_cypher[index % len(key_cypher)]

        # Right-shift the message character
        encrypted_char_index = (message_char_index + index_shift) % len(printable)

        # Add encrypted character to the message
        encrypted_message += printable[encrypted_char_index]

    return encrypted_message

def simple_decrypt(message, key):
    """ Uses key values to unshift the characters in the encrypted message
        and return the original plaintext

        Input: key <printable string> 
               message <printable string> 
        Output: decrypted_message <printable string> 
    """
    key_cypher = [ord(character) for character in key]
    decrypted_message = ""
    for index, character in enumerate(message):
        # Get the index of a character in message
        message_char_index = printable.index(character)

        # Calculate shift amount from the key
        index_shift = key_cypher[index % len(key_cypher)]

        # Left-shift the message character
        encrypted_char_index = (message_char_index - index_shift) % len(printable)

        # Add decrypted character to the message
        decrypted_message += printable[encrypted_char_index]

    return decrypted_message
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", type=str, help="input message", default="Sample")
    parser.add_argument("-k", "--key", type=str, help="symmetric key", default="Secret")
    parser.add_argument("-d", "--decrypt", action='store_true')
    args = parser.parse_args()

    if not args.decrypt:
        encrypted = simple_encrypt(args.message, args.key)
        print("Encrypted message: {}\nDecrypted message: {}".format(encrypted, simple_decrypt(encrypted, args.key)))
    else:
        simple_decrypt(args.message, args.key)

if __name__ == '__main__':
    main()
