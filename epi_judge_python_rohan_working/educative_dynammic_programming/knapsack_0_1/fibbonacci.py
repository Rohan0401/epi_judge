
def _calculateFibonacci(n):
    # base case recursion

    if n < 2:
        return n


    return calculateFibonacci(n-1) + (n-2)

###
def memo_calculateFibonacci(n):
    # base case recursion
    memo = [-1 for _ in range(n+1)]
    return calculateFibonacciRecur(memo, n)

def calculateFibonacciRecur(memo, n):
    if n < 2:
        return n

    if memo[n] >= 0:
        return memo[n]
    memo[n] =  calculateFibonacciRecur(memo, n - 1) + calculateFibonacciRecur(memo, n -2)

    return memo[n]


def calculateFibonacci(n):

    dp = [0, 1]

    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])

    return dp[-1]

def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()
