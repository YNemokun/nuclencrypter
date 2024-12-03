from encoder import encrypt
from decoder import decrypt
import sys
import numpy as np
import random

if len(sys.argv) != 4:
    print("Usage: python3 main.py <message.txt> <encode_output_file> <decode_output_file")
    sys.exit(1)

## Encode a list of characters (phone number or names) into an amino acid sequence 

input_file = sys.argv[1]
encode_output_file = sys.argv[2]
decode_output_file = sys.argv[3]

with open(input_file, 'r') as input_messages:
    with open(encode_output_file, 'w') as file_out:
        for line in input_messages:
            message = line.strip() #string of message to encode
            encrypted, password, pattern = encrypt(message)
            file_out.write(f"{encrypted} {password} {pattern}\n")
# Read input file

# Apply encoder method

# Output amino acid sequence file



## Decode an amino acid sequence into a message (phone number or names)
# Read input file
with open(encode_output_file, 'r') as input_messages:
    with open(decode_output_file, 'w') as file_out:
        for line in input_messages:
            message = line.strip() # message to decode
            decrypted = decrypt(message)
            file_out.write(decrypted)
            file_out.write('\n')

# Apply decoder method

# Output decrypted message
