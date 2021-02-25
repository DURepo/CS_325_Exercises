'''
 time complexity would be O(n^2).
'''
def rodCutting_bottomup(n, prices):
  # Create a dp array the size of (n+1)
  #dp[1] = best price for length 1 and so on...
  dp = [0 for _ in range(n + 1)]

  # starting from rod of length 1, find optimal answer to all subproblems
  for length in range(1, n + 1):
    max_val = 0
    # for a rod of length i, we can find what cuts give max answer since we have answer to all smaller cuts
    for possible_cut in range(length):
        #If we find a better price replace max value and solution array sol[i] to point to the length that gave us max value
        #since the index of possible cut starts with 0, to get its value we need to do +1 when accessing dp table
        if((prices[possible_cut] + dp[length-(possible_cut+1)]) > max_val):
            max_val = prices[possible_cut] + dp[length-(possible_cut+1)]

    dp[length] = max_val
  # return answer to n length rod
  return dp[n]
