'''
source: https://www.educative.io/courses/dynamic-programming-in-python/xoG0Lmq84yn
'''
def rodCutting_topdown_helper(n, prices, memo):
  if n<0:
    return 0
  if n in memo:
    return memo[n]
  max_val = 0
  for i in range(1,n+1):
      max_val = max(max_val, prices[i-1] + rodCutting_topdown_helper(n - i, prices, memo))
  memo[n] = max_val
  return memo[n]

def rodCutting_topdown(n, prices):
  memo = {}
  return rodCutting_topdown_helper(n, prices, memo)
