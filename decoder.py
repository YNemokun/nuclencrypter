## Functions to decompose an amino acid sequence into its DNA sequence form, and then decrypt it to the original message
import sys

def reverse_bwt(bwt, pos): # Step 1: reverse bwt operations
    # add $ back to the string
    bwt = bwt[:pos] + "$" + bwt[pos:]
    # count the frequency of each character
    freq = {}
    for s in bwt:
        freq[s] = freq.get(s, 0) + 1

    freq = dict(sorted(freq.items()))

    # make first column
    firstCol = ""
    for i in freq.keys():
        firstCol += i*freq[i]

    text = ""

    row = 0
    rank = {}
    # first row's last character is the last character of the message
    while bwt[row] != '$':
        text = text + bwt[row]
        rank = bwt.count(bwt[row], 0, row)
        row = firstCol.find(bwt[row]) + rank
    return text[::-1]

def reverse_permute(dna): # Step 2: reverse permutations
  # permuted pattern
  pattern = [1, 3, 0, 2]
  permuted = []
  substr_len = len(dna) // 4
  substrings = []
  start = 0
  for i in range(4):
    end = start + substr_len 
    substrings.append(dna[start:end])
    start = end
  
  for i in range(len(pattern)):
    permuted.insert(pattern[i], substrings[i])  
  
  return ''.join(permuted)


def left_shift(dna): # Step 3
  return dna[1:] + dna[0]


def reverse_complement(dna): # Step 4
  dna = dna[::-1]
  dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
  result = []
  for char in dna:
    if char in dict:
      result.append(dict[char])
  result = ''.join(result)
  return result


def decode(message): # Step 5
  decode_dict = {
    "ACAT": "a", "AAAA": "y", "ATAA": "W", "AGAG": "{",
    "ACTG": "b", "AATT": "z", "ATTT": "X", "AGTA": "[",
    "ACCC": "c", "AACC": "A", "ATCG": "Y", "AGCG": "}",
    "ACGA": "d", "AAGG": "B", "ATGC": "Z", "AGGG": "]",
    "TCAT": "e", "TAAT": "C", "TTAA": "0", "TGAA": "|",
    "TCTG": "f", "TATG": "D", "TTTT": "1", "TGTT": "\\",
    "TCCG": "g", "TACC": "E", "TTCC": "2", "TGCG": "+",
    "TCGT": "h", "TAGA": "F", "TTGG": "3", "TGGC": "=",
    "CCAG": "i", "CAAT": "G", "CTAT": "4", "CGAA": "_",
    "CCTA": "j", "CATG": "H", "CTTG": "5", "CGTT": "-",
    "CCCG": "k", "CACG": "I", "CTCC": "6", "CGCC": ")",
    "CCGG": "l", "CAGT": "J", "CTGA": "7", "CGGG": "(",
    "GCAA": "m", "GAAG": "K", "GTAT": "8", "GGAT": "*",
    "GCTT": "n", "GATA": "L", "GTTG": "9", "GGTG": "&",
    "GCCG": "o", "GACG": "M", "GTCG": "<", "GGCC": "^",
    "GCGC": "p", "GAGG": "N", "GTGT": ">", "GGGA": "%",
    "ACTC": "q", "AATA": "O", "ATTA": ",", "AGTT": "$",
    "ACCG": "r", "AACG": "P", "ATCC": ".", "AGCC": "#",
    "TCTC": "s", "TATC": "Q", "TTTA": "?", "TGTA": "@",
    "TCCC": "t", "TACG": "R", "TTCG": "/", "TGCC": "!",
    "CCTT": "u", "CATC": "S", "CTTC": ":", "CGTA": "~",
    "CCCC": "v", "CACC": "T", "CTCG": ";", "CGCG": "`",
    "GCTA": "w", "GATT": "U", "GTTC": "“", "GGTC": "€",
    "GCCC": "x", "GACC": "V", "GTCC": "‘", "GGCG": "£"
}
  decode = []

  for i in range(0, len(message) - 3, 4):
    decode += decode_dict[message[i:i + 4]]
  return ''.join(decode)



def decrypt(message):
  msg = message.split(" ")
  pos = int(msg[1])
  decoded = reverse_bwt(msg[0], pos)
  reverse_permutation = left_shift(reverse_permute(decoded))
  reverse_comp = reverse_complement(reverse_permutation)
  decrypted = decode(reverse_comp)
  return decrypted


def main():
  if len(sys.argv) != 3:
    print("Usage: python3 decoder.py <messages.txt> <output_file>")
    sys.exit(1)
  
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  
  with open(input_file, 'r') as input_messages:
    with open(output_file, 'w') as file_out:
      for line in input_messages:
        message = line.strip() # message to decode
        decrypted = decrypt(message)
        file_out.write(decrypted)
        file_out.write('\n')
      
  
if __name__ == "__main__":
   main()