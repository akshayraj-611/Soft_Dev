from string import ascii_lowercase

secret_mapping = {
      char: "cR" + char + "7"
      for char in ascii_lowercase
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
        if secret_text[i:i+2] == "cR" and i + 3 < len(secret_text):
            token = secret_text[i:i+4]  
            if token in reverse_mapping:
                decoded.append(reverse_mapping[token])
                i += 4
                continue
        
        decoded.append(secret_text[i])
        i += 1
    
    return "".join(decoded)


while True:
    en_or_de = int(input("Do you want to Encode or Decode a message? Enter 1 to encode or 0 to decode..."))
    if en_or_de == 1 :
        msg = input("Enter a message to be encoded into the secret Language: ")
        encoded = encode_secret(msg)
        print("Original:", msg)
        print("Encoded :", encoded)
        break
    elif en_or_de == 0:
        msg = input("Enter a message in your secret Language to be Decoded: ")
        decoded = decode_secret(msg)
        print("Original:", msg)
        print("Decoded :", decoded)
        break

    else :
        print ("Invalid Input..try again")
