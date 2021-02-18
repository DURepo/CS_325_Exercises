'''
Bottom-up approach
https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
'''
def lcs_bottomup(str1, str2):
    m = len(str1)
    n = len(str2)

    # create a 2-D dynamic programming table of size m+1 X n+1
    cache = [[0 for x in range(n+1)] for x in range(m+1)]

    # building the matrix
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                cache[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j]= max(cache[i-1][j] , cache[i][j-1])

    return cache[m][n]


#print(lcs_bottomup("abcde", "ac"))
