from string import ascii_lowercase

secret_mapping = {
    char: f"cR{char}{idx % 10}"
    for idx, char in enumerate(ascii_lowercase)
}

reverse_mapping = {v: k for k, v in secret_mapping.items()}

def encode_secret(text):
    encoded = []
    for ch in text:
        if ch in secret_mapping:
            encoded.append(secret_mapping[ch])
        else:
            encoded.append(ch)
    return "".join(encoded)

def decode_secret(secret_text):
    decoded = []
    i = 0

    while i < len(secret_text):
        starts_with_cr = secret_text.startswith("cR", i)
        has_room = i + 3 < len(secret_text)
        next_is_letter = has_room and secret_text[i+2].isalpha()
        next_is_digit = has_room and secret_text[i+3].isdigit()

        if starts_with_cr and has_room and next_is_letter and next_is_digit:
            decoded.append(secret_text[i+2])
            i += 4
            continue

        decoded.append(secret_text[i])
        i += 1

    return "".join(decoded)

while True:
    try:
        en_or_de = int(input("Encode or Decode? Enter 1 for encode, 0 for decode: "))
    except ValueError:
        print("Please enter 1 or 0.")
        continue

    if en_or_de == 1:
        msg = input("Enter a message to encode: ")
        encoded = encode_secret(msg)
        print("Original:", msg)
        print("Encoded :", encoded)
        break

    elif en_or_de == 0:
        msg = input("Enter a message to decode: ")
        decoded = decode_secret(msg)
        print("Original:", msg)
        print("Decoded :", decoded)
        break

    else:
        print("Invalid choice — try again.")
