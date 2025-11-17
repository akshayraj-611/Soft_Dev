import re
from string import ascii_lowercase

encrypted_messages = [
    "rdUYjcfruqjUYrfnqAYrfnqPYhtr",
    "otmsPYitjAYrfnqUYzxPYhtr"
]

SHIFT = 5  

symbols = {
    "UY": "-",
    "AY": "@",
    "PY": "." }

def shift_letter(c, shift):
    idx = ascii_lowercase.index(c)
    return ascii_lowercase[(idx - shift) % 26]

def apply_shift(word, shift):
    return ''.join(shift_letter(c, shift) for c in word)

def decode_message(msg, shift, symbols):
    decoded = re.sub('[a-z]+', lambda match: apply_shift(match.group(), shift), msg) #re.sub(pattern, replacement, message)
    for code, symbol in symbols.items():
        decoded = decoded.replace(code, symbol)
    return decoded

for idx,msg in enumerate(encrypted_messages):
    print(f"Encrypted Message {idx+1} : {encrypted_messages[idx]}")
    print(f"Decrypted Messsage {idx+1}: {decode_message(msg, SHIFT, symbols)}")


