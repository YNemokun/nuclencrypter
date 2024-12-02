import numpy as np
import sys

def find_edit_distance(a, b):
  dp = np.zeros((len(a) + 1, len(b) + 1))    
  dp[1:, 0] = range(1, len(a) + 1)
  dp[0, 1:] = range(1, len(b) + 1)
  for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
      delta = (0 if a[i - 1] == b[j - 1] else 1)
      dp[i,j] = min(dp[i-1, j] + 1, dp[i, j-1] + 1, dp[i - 1, j - 1] + delta)
  return dp[len(a), len(b)]

def find_optimal(read_list):
  score_list = np.zeros(len(read_list))
  for i in range(1, len(read_list)):
    for j in range(i):
      ed = find_edit_distance(read_list[i], read_list[j])
      score_list[i] += ed
      score_list[j] += ed
  return np.argmin(score_list)
