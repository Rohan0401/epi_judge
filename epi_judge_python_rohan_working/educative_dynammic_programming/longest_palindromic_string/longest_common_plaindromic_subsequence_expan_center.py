def find_LPS(s):
    maxLen = 1
    start = 0

    length = len(s)

    low = 0
    high = 0

    for i in range(1, length):

        low = i -1
        high = i

        while low >= 0 and high < length and s[low] == s[high]:
            if high - low + 1 > maxLen:
                start = low
                maxLen = high - low + 1
            low -= 1
            high += 1
        # odd length
        low = i -1
        high = i + 1

        while low >= 0 and high < length and s[low] == s[high]:
            if high - low + 1 > maxLen:
                start = low
                maxLen = high - low + 1
            low -= 1
            high += 1

    print(s[start: start+ maxLen])





    return maxLen
#
print(find_LPS("abdbea"))
print(find_LPS("cddpd"))
print(find_LPS("pqr"))
#
# n = 5
#
# for i in range(n-1, -1, -1):
#     print(i)
