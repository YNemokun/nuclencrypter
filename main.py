from encoder import encrypt
from decoder import decrypt
from sequencing_simulator import simulate_sequencing
from local_alignment import parser
import sys
import numpy as np
import random

# Usage: 
# encode: python3 main.py -e <message.txt> <encode_output_file> 
# decode: python3 main.py -d <encoded_message.txt> <decode_output_file> 
if len(sys.argv) != 4:
    print("Usage: python3 main.py -e <message.txt> <encode_output_file> or python3 main.py -d <encoded_message.txt> <decode_output_file> ")
    sys.exit(1)

flag = sys.argv[1]
if flag != 'e' and flag != 'd':
    print("missing flag")
    sys.exit(1)
    
input_file = sys.argv[2]

#encrypt customized messages into dna sequences
if flag == 'e':
    encode_output_file = sys.argv[3]
    with open(input_file, 'r') as input_messages:
        with open(encode_output_file, 'w') as file_out:
            for line in input_messages:
                message = line.strip() #string of message to encode
                #encrypted, password, pattern = encrypt(message)
                encrypted, pattern = encrypt(message)
                #file_out.write(f"{encrypted} {password} {pattern}\n")
                file_out.write(f"{encrypted} {pattern}\n")

#simulate sequencing, find optimal sequence, and decode an encrypted dna sequences into messages
elif flag == 'd':
    decode_output_file = sys.argv[3]
    #open encrypted DNA for simulated sequencing 
    simulated_sequences = 'simulated_seqs.txt'
    simulate_sequencing(input_file, simulated_sequences)
    #find optimal sequence and decrypt 
    optimal_sequences = 'optimal_seqs.txt'
    with open(decode_output_file, 'w') as file_out:
        parser(simulated_sequences, optimal_sequences)
        with open(optimal_sequences, 'r') as optimal_seqs:
            for line in optimal_seqs:
                message = line.strip() # message to decode
                decrypted = decrypt(message)
                file_out.write(decrypted)
                file_out.write('\n')

