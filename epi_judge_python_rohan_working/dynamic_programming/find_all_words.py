from collections import Counter
def find_string(input_string, input_words):
    if len(input_string) <= 0:
        return True

    if len(input_words) <= 0:
        return False
    word_count = Counter(input_words)

    def helper(s):

        if len(s) == 0:
            return True

        for i in range(len(s)):
            if s[:i+1] in word_count and word_count[s[:i+1]] == 1:
                print(s[:i+1])
                word_count[s[:i+1]] -= 1
                out_put = helper(s[i+1:])
                if out_put:
                    return True
                else:
                    word_count[s[:i+1]] += 1




        return False
    return helper(input_string)


print("Print bool :", find_string("helloworldhello", ["hello", "world", "tea"]))

def find_string(input_string, input_words):

    if len(input_string) <= 0:
        return True

    if len(input_words) <= 0:
        return False

    dp = [False] * (len(input_string) + 1)

    dp[0] = True

    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            if dp[i] == True and input_string[i:j+1] in input_words:
                dp[j+1] = True
    return dp[-1]

print("Print bool :", find_string("helloworldhello", ["hello", "world", "tea"]))
