
def longest_common_palindrome(s):
    n = len(s)

    dp = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (i == j):
                dp[i][j] = True


