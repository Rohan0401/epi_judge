from __future__ import print_function


def solve_knapsack(profits, weights, capacity):
  n = len(profits)
  # basic checks
  if capacity <= 0 or n == 0 or len(wieghts) != n:
      return 0

  # create a dp table
  dp = [[0 for c in range(capacity+1)] for x in range(n)]

  # column with 0 capacity we have 0 profit
  for c in range(capacity):
      dp[0][c] = 0

  # make two choices 1 include the element add its value and reduce its weight or exclude the element with same weight with 0 profit

  for i in range(n):
      for c in range(capacity+1):
          profit1, profit2 = 0, 0
          # exclude -ve
          if weights[i] <= c:
              profit1 = dp[i][c - weights[i]] + profits[i]
          profit2 = dp[i-1][c]

          dp[i][c] = max(profit1, profit2)

  print_the_weights(dp, profits, weights, capacity)

  return dp[n-1][capacity]

def print_the_weights(dp, profits, weights, capacity):
    n = len(weights)
    totalProfit = dp[n-1][capacity]
    for i in range(n-1, 0 , -1):
        if totalProfit != dp[i-1][capacity]:
            print(weights[i])
            capacity -= weights[i]
            totalProfit -= profits[i]

    print()

def main():
  print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
  print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()
