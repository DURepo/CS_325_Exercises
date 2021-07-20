# Print weights of items that form the optimal solution
def unbound_knapsackOptimalSolution(W, n, weights, values):
    dp = [0]*(W+1)
    sol = [0]*(W+1)

    for x in range(1,W+1):
        for i in range(n):
            wi = weights[i]
            if wi <= x:
                if((dp[x-wi] + values[i] ) > dp[x]):
                    dp[x]=dp[x-wi] + values[i]
                    sol[x]= wi


    w = W
    solution = []
    while w>0:
        solution.append(sol[w])
        w = w-sol[w]

    return solution


print(unbound_knapsackOptimalSolution(10,5,[4,9,3,5,7], [10,25,13,20,8]))
