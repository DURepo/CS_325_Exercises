def makechangeBF(coins, amount):
    if(amount == 0): return 0
    result = amount+1 #some arbitary huge number that cannot be the answer

    for i in range(len(coins)):
        if(coins[i] <= amount):
            result = min(result, makechangeBF(coins, amount-coins[i]) + 1)
    return result


print(makechangeBF([1,3,5] , 9 ))
