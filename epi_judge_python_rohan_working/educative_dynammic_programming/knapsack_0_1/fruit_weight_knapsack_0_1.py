def solve_knapsack(profits, weights, capacity):
  return knapsack_recursive(profits, weights, capacity, 0)

# def knapsack_recursive(profits, weights, capacity, currentIndex):
#
#     # base case
#     if currentIndex >= len(profits) or capacity <= 0:
#         return 0
#     profit1 = 0
#     if weights[currentIndex] <= capacity:
#         profit1 = profits[currentIndex] + knapsack_recursive(profits, weights, capacity - weights[currentIndex], currentIndex+1)
#     profit2 = 0
#
#     profit2 = knapsack_recursive(profits, weights, capacity, currentIndex+1)
#
#     return max(profit1, profit2)

def _solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(len(profits))] for y in range(capacity+1)]
    return knapsack_recursive_memo(dp , profits, weights, capacity, 0)


def knapsack_recursive_memo(dp , profits, weights, capacity, currentIndex):
    # base condition
    if currentIndex >= len(profits) or capacity <= 0:
        return 0
    # if we have not solved the problem return the memeory
    if dp[capacity][currentIndex] != -1:
        return dp[capacity][currentIndex]

    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive_memo(dp , profits, weights, capacity - weights[currentIndex], currentIndex+1)
    profit2 = 0

    profit2 = knapsack_recursive_memo(dp, profits, weights, capacity, currentIndex+1)

    dp[capacity][currentIndex] = max(profit1, profit2)

    return dp[capacity][currentIndex]

def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)

    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    # DP array
    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    # for 0 column we have 0 capacity
    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight then we will take it is as it not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1,n):
        for c in range(1,capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c - weights[i]]
            profit2 = dp[i-1][c]

            # take max
            dp[i][c] = max(profit1, profit2)

    return dp[n-1][capacity]




def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
