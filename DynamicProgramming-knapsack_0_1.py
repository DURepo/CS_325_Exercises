def knapsack_0_1(W, n, weights, values):
    dp = [[0 for x in range(n+1)] for x in range(W+1)]
    for x in range(1,W+1):
        for i in range(1,n+1):
            dp[x][i]=dp[x][i-1]
            wi = weights[i-1]
            vi = values[i-1]
            if x >= wi:
                dp[x][i] = max(dp[x][i] , dp[x-wi][i-1] + vi)
    
    return dp[W][n]

print(knapsack_0_1(10, 5 ,[4, 9, 3, 5, 7], [10, 25, 13, 20, 8] ))
