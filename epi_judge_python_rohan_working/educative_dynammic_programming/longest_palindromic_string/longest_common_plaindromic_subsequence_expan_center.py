def find_LPS(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    max_len = -1
    for i in range(n-1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            elif i+1 == j and s[i] == s[j]:
                dp[i][j] = 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            max_len = max(max_len, dp[i][j])
    #printing LPS
    index = dp[0][n-1]



    return max_len
#
print(find_LPS("abdbea"))
print(find_LPS("cddpd"))
print(find_LPS("pqr"))
#
# n = 5
#
# for i in range(n-1, -1, -1):
#     print(i)
