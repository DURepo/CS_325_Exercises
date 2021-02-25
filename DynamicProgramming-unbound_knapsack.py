def unbound_knapsack(W, n, weights, values):
    dp = [0]*(W+1)

    for x in range(1, W+1):

        for i in range(n):
            wi = weights[i]
            if wi <= x:
                dp[x] = max(dp[x] , dp[x-wi] + values[i])

    return dp[W]


print(unbound_knapsack(10,5,[4,9,3,5,7], [10,25,13,20,8]))
