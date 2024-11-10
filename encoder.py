## Functions to encrypt a message into a DNA sequence
# 1) encoding table 2) reverse complement 3) right shift 4) permutation 5) BWT
import sys

def encode(message): #step 1
  encode_dict = {
    "a": "ACAT", "y": "AAAA", "W": "ATAA", "{": "AGAG",
    "b": "ACTG", "z": "AATT", "X": "ATTT", "[": "AGTA",
    "c": "ACCC", "A": "AACC", "Y": "ATCG", "}": "AGCG",
    "d": "ACGA", "B": "AAGG", "Z": "ATGC", "]": "AGGG",
    "e": "TCAT", "C": "TAAT", "0": "TTAA", "|": "TGAA",
    "f": "TCTG", "D": "TATG", "1": "TTTT", "\\": "TGTT",
    "g": "TCCG", "E": "TACC", "2": "TTCC", "+": "TGCG",
    "h": "TCGT", "F": "TAGA", "3": "TTGG", "=": "TGGC",
    "i": "CCAG", "G": "CAAT", "4": "CTAT", "_": "CGAA",
    "j": "CCTA", "H": "CATG", "5": "CTTG", "-": "CGTT",
    "k": "CCCG", "I": "CACG", "6": "CTCC", ")": "CGCC",
    "l": "CCGG", "J": "CAGT", "7": "CTGA", "(": "CGGG",
    "m": "GCAA", "K": "GAAG", "8": "GTAT", "*": "GGAT",
    "n": "GCTT", "L": "GATA", "9": "GTTG", "&": "GGTG",
    "o": "GCCG", "M": "GACG", "<": "GTCG", "^": "GGCC",
    "p": "GCGC", "N": "GAGG", ">": "GTGT", "%": "GGGA",
    "q": "ACTC", "O": "AATA", ",": "ATTA", "$": "AGTT",
    "r": "ACCG", "P": "AACG", ".": "ATCC", "#": "AGCC",
    "s": "TCTC", "Q": "TATC", "?": "TTTA", "@": "TGTA",
    "t": "TCCC", "R": "TACG", "/": "TTCG", "!": "TGCC",
    "u": "CCTT", "S": "CATC", ":": "CTTC", "~": "CGTA",
    "v": "CCCC", "T": "CACC", ";": "CTCG", "`": "CGCG",
    "w": "GCTA", "U": "GATT", "“": "GTTC", "€": "GGTC",
    "x": "GCCC", "V": "GACC", "‘": "GTCC", "£": "GGCG"
  }
  encoded = []
  for char in message:
    encoded += encode_dict[char]
  return ''.join(encoded)


def reverse_complement(dna): #step 2
  dna = dna[::-1]
  dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
  result = []
  for char in dna:
    if char in dict:
      result.append(dict[char])
  result = ''.join(result)
  return result

def right_shift(dna): #step 3
  return dna[-1] + dna[:-1]
  
def permute(dna): #step 4
  permuted = []
  substr_len = len(dna) // 4
  substrings = []
  start = 0
  for i in range(4):
    end = start + substr_len 
    substrings.append(dna[start:end])
    start = end
  pattern = [1, 3, 0, 2]
  for p in pattern:
    permuted += substrings[p] 
  return ''.join(permuted)

def get_bwt(dna): #step 5 
  dna += '$'
  bwm = [dna[i:] + dna[:i] for i in range(len(dna))]
  bwm = sorted(bwm)
  bwt = ''.join(rotation[-1] for rotation in bwm) 
  dollar_index = bwt.index('$') 
  bwt = bwt.replace("$", "")
  return bwt, dollar_index
  

def encrypt(message): #function to encrypt a given message
  encoded = encode(message)
  reversed = reverse_complement(encoded)
  permuted = permute(right_shift(reversed))
  encrypted, password = get_bwt(permuted)
  return encrypted, password


def main():
  if len(sys.argv) != 3:
    print("Usage: python3 excoder.py <messages.txt> <output_file>")
    sys.exit(1)
  
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  
  with open(input_file, 'r') as input_messages:
    with open(output_file, 'w') as file_out:
      for line in input_messages:
        message = line.strip() #string of message to encode
        encrypted, password = encrypt(message)
        file_out.write(f"{encrypted} {password}\n")
      
  
if __name__ == "__main__":
   main()