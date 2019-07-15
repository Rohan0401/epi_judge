def find_min_operations(s1, s2):
    n1, n2 = len(s1), len(s2)

    dp = [[-1 for x in range(n2+1)] for y in range(n1+1)]

    # if s2 empty make the length full of char s1
    for i1 in range(n1+1):
        dp[i1][0] = i1
    # if s1 is empty

    for i2 in range(n2+1):
        dp[0][i2] = i2

    for i1 in range(1, n1+1):
        for i2 in range(1, n2+1):
            if s1[i1-1] == s2[i2-1]:
                dp[i1][i2] = dp[i1-1][i2-1] # if same
            else:
                dp[i1][i2] = 1 + min(dp[i1][i2-1], min(dp[i1-1][i2],  # insert
                                          dp[i1-1][i2-1] )) # replace
    return dp[n1][n2]


print(find_min_operations("bat", ""))
print(find_min_operations("abdca", "cbda"))
print(find_min_operations("passpot", "ppsspqrt"))
