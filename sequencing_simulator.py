import sys
import random

def introduce_errors(sequence, substitution_rate=0.001, indel_rate=0.0001): #return dna string with error introduced
  bases = ['A', 'C', 'G', 'T']
  new_sequence = []

  for base in sequence:
    rand = random.random()
    if rand < substitution_rate: #substitution
      new_sequence.append(random.choice([b for b in bases if b != base]))
    elif rand < substitution_rate + indel_rate: #insertion
      new_sequence.append(base)
      new_sequence.append(random.choice(bases))
    elif rand < substitution_rate + 2 * indel_rate: #deletion
      continue  #skip adding this base (deletion)
    else:  #no change
      new_sequence.append(base)
  
  return ''.join(new_sequence)


def simulate_sequencing(input_file, output_file): #function to simulate sequencing a DNA 5 times (with possible sequencing errors introduced)
  with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
      stripped_line = line.strip()
      if stripped_line: #skip empty lines
        parts = stripped_line.split(maxsplit=2)
        sequence = parts[0]
        key = parts[1]
        pattern = parts[2]
        for i in range(5):
          error_sequence = introduce_errors(sequence, 0.1, 0.05)
          outfile.write(f"{error_sequence} {key} {pattern}\n")

def main():
  if len(sys.argv) != 3:
    print("Usage: python3 sequencing_simulator.py <input.txt> <output.txt>")
    sys.exit(1)
    
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  simulate_sequencing(input_file, output_file)
  
if __name__ == "__main__":
  main()
  