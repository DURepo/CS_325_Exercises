
def optimalsolution_LCS(str1, str2, cache):
    # Cache is already filled out 2-D array solution
    m = len(str1)
    n = len(str2)
    lcs = []

    while m>0 and n>0:
        if(str1[m-1] == str2[n-1]):
            #append str1[m] to lcs
            lcs.append(str1[m-1])
            m -=1
            n -=1
        elif(cache[m][n] == cache[m][n-1]): n= n-1
        else: m = m-1

    #lcs has the solution in reverse order,
    # since we traversed from the last characters of two strings
    # We will get our solution by reversing the value of lcs
    return ''.join(reversed(lcs))



def lcs(str1, str2):
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

    return  optimalsolution_LCS(str1, str2, cache)


print(lcs("ABCDGH", "AEDFHR"))
