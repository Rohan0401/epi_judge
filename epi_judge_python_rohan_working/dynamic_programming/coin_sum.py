import math
def solve(coins, x):

    # for negetive coins
    if x < 0:
        return -math.inf
    # base case
    if x == 0:
        return 0
    # base_case
    best_sol = math.inf

    for coin in coins:
        best_sol = min(best_sol, solve([]x - coin)+ 1)

    return best_sol


print(solve([1.3,5,7], 10))
