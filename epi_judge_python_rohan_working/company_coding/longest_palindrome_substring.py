def longest_palindromic_substring(s):
    # loop over each char once to find the longest palindrome
    if len(s) <= 1:
        return s
    s_start = s[0]
    longest_pali = s_start

    for i in range(len(s)):
        temp = expand(s, i, i)
        if len(temp) > len(longest_pali):
            longest_pali = temp
        temp = expand(s, i, i+1)
        if len(temp) > len(longest_pali):
            longest_pali = temp

    return longest_pali







def expand(s, l , r):
    # provides the longest possible palindrome keeping a char in center
    while (l >= 0 and r < len(s) and s[l] == s[r]):
        l -= 1
        r += 1
    return s[l+1:r]

def main():
    print(longest_palindromic_substring("abbcfsdff"))

main()
