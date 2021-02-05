# https://cryptopals.com/sets/1/challenges/1
# https://docs.python.org/3/library/base64.html

import binascii
import base64

def hexToBase64(s):
    hexadecimalRepresentation = binascii.unhexlify(s)
    return base64.b64encode(hexadecimalRepresentation).decode("utf8")
value = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print(hexToBase64(value))
