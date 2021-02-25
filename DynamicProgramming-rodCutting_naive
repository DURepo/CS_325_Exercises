
'''
recursive solution Time complexity - O(2^n)
source: https://www.educative.io/courses/dynamic-programming-in-python/xoG0Lmq84yn
'''

def rodCutting_naive(n, prices):
  if n<0:
    return 0
  max_val = 0
  for i in range(1,n+1):
      max_val = max(max_val, prices[i-1] + rodCutting_naive(n - i, prices))
  return max_val
