'''
LCS recursive
https://www.geeksforgeeks.
'''

def lcs_BF_helper(s1, s2, m,n):
    if m < 0 or n < 0:
        return 0;
    elif s1[m] == s2[n]:
        return 1 + lcs_BF_helper(s1, s2 , m-1, n-1)
    else:
        return max(lcs_BF_helper(s1, s2, m-1 , n), lcs_BF_helper(s1, s2, m, n-1))

def lcs_BF(str1, str2):
    return lcs_BF_helper(str1,str2, len(str1)-1, len(str2)-1)

print(lcs_BF("abcde", "ac"))
