def solve_rod_cutting(lengths, prices,n):
    lengthCounts = len(lengths)

    # base checkks

    if n <= 0 or lengthCounts == 0 or len(prices) != lengthCounts:
        return 0

    dp = [[-1 for x in range(n+1)] for y in range(lengthCounts) ]

    # process for all prices
    for i in range(lengthCounts):
        for length in range(n+1):
            p1, p2 = 0, 0
            if lengths[i] <= length:
                p1 = prices[i] + dp[i][length - lengths[i]]
            p2 = dp[i-1][length]

            dp[i][length] = max(p1, p2)

    return dp[lengthCounts-1][n]

def main():
  print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


main()
