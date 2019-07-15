def find_string(s, word_dict):

    if len(s) <= 0 or len(word_dict) <= 0:
        return True
    dp = [False] * (len(s) + 1)

    dp[0] = True

    for i in range(1, len(s)+ 1):
        for k in range(i):
            if s[k] and s[k:i] in word_dict:
                dp[i] = True
    print(dp)
    return dp[len(s)]

print(find_string("leetcode", set(["leet", "code"])))
