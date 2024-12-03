import numpy as np
import sys

def find_edit_distance(a, b): #dynamic programming for pairwise local alignment
  dp = np.zeros((len(a) + 1, len(b) + 1))    
  dp[1:, 0] = range(1, len(a) + 1)
  dp[0, 1:] = range(1, len(b) + 1)
  for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
      delta = (0 if a[i - 1] == b[j - 1] else 1)
      dp[i,j] = min(dp[i-1, j] + 1, dp[i, j-1] + 1, dp[i - 1, j - 1] + delta)
  return dp[len(a), len(b)]

def find_optimal(read_list): #find optimal sequence by minimizing edit distance
  score_list = np.zeros(len(read_list))
  for i in range(1, len(read_list)):
    for j in range(i):
      ed = find_edit_distance(read_list[i][0], read_list[j][0]) #read_list[i][0] = read, [1] == bwt index (key), [2] == pe®mutation order (password)
      score_list[i] += ed
      score_list[j] += ed
  return np.argmin(score_list)

def parser(input_file, output_file): #preprocess input data
  with open(input_file, 'r') as in_f, open(output_file, 'w') as out_f:
    while True:
      lines = (in_f.readline() for i in range(5))
      chunk = [line.strip() for line in lines if line.strip()]
      if not chunk: break
      processed_chunk = []
      for line in chunk:
        entry = line.split(maxsplit=2)
        sequence = entry[0]
        key = int(entry[1])
        pattern = eval(entry[2])
        processed_chunk.append((sequence, key, pattern)) #list of 5 tuples
      optimal_idx = find_optimal(processed_chunk)
      optimal_read = processed_chunk[optimal_idx]
      out_f.write(f"{optimal_read[0]} {optimal_read[1]} {optimal_read[2]}\n") 
        

def main():
  if len(sys.argv) != 3:
    print("Usage: python3 local_alignment.py <input.txt> <output.txt>")
    sys.exit(1)
    
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  parser(input_file, output_file)


if __name__ == "__main__":
  main()