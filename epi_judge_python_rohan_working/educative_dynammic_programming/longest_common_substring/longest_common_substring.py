def find_LCS_length(s1, s2):
  m, n = len(s1), len(s2)
  if m <= 0 or n <= 0:
     return 0
  dp = [[0 for x in range(n+1)] for y in range(m+1)]
  max_len = 0
  for i in range(m):
    for j in range(n):
      if s1[i] == s2[j]:
        dp[i][j] = 1 + dp[i-1][j-1]
        max_len = max(max_len, dp[i][j])


  return max_len




def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))


main()
