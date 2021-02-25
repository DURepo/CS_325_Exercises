def makechange(coins, amount):

    min_count_table = [amount+1]*(amount+1) # setting array elements to some large value that is not possible answer
    coin_used = [ 0 for _ in range(amount+1)]

    min_count_table[0] = 0 # setting the base case

    for amnt in range(1, amount+1):  # iterate through all possible amount values from base case
        for coin_itr in range(0, len(coins)): #find the number of coins needed for each coin denomination
            coin_val = coins[coin_itr]
            if(coin_val <= amount): # if denomination value is less than amount then we can use the coin
                if(min_count_table[amnt-coin_val]+1 < min_count_table[amnt]): #if we found new best solution
                    min_count_table[amnt] = min_count_table[amnt-coin_val]+1
                    coin_used[amnt] = coin_val

    # we have a valid count of coins if min_count_table[amount] is valid
    if min_count_table[amount] > amount: result = -1
    else: result = min_count_table[amount]

    #Print the coins to be used
    while amount>0:
        print(coin_used[amount])
        amount = amount-coin_used[amount]


print(makechange([1,3,5], 8))
