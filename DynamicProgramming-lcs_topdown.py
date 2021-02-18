'''
Top-Down approach
https://www.geeksforgeeks.org/longest-common-subsequence-dp-using-memoization/
'''
def lcs_topdown_helper(s1, s2, m, n, dp):

    #base case
    if(m == 0 or n == 0):
        return 0

    #If the subproblem already computed return it
    if(dp[m-1][n-1] != -1): return dp[m-1][n-1]

    #if the chars match, store result
    if(s1[m-1] == s2[n-1]):
        dp[m-1][n-1] = 1 + lcs_topdown_helper(s1, s2, m-1, n-1, dp)
        return dp[m-1][n-1]

    else:
        dp[m-1][n-1] = max(lcs_topdown_helper(s1, s2, m-1, n ,dp) , lcs_topdown_helper(s1, s2, m, n-1, dp))
        return dp[m-1][n-1]

def lcs_topdown(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[-1 for x in range(n+1)] for x in range(m+1)]
    return lcs_topdown_helper(str1,str2, m, n, dp)

print(lcs_topdown("abcde", "ace"))
