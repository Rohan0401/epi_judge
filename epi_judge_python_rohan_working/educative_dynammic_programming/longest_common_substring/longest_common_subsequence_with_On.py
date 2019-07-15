def find_LCS_length(s1, s2):
  m, n = len(s1), len(s2)
  if m <= 0 or n <= 0:
     return 0
  # only take previous row
  dp = [[0 for x in range(n+1)] for y in range(2)]
  max_len = 0
  for i in range(m):
    for j in range(n):
      if s1[i] == s2[j]:
        dp[i%2][j] = 1 + dp[(i-1)%2][j-1]
      else:
          dp[i%2][j] = max(dp[(i-1)%2][j], dp[i%2][j-1])
      max_len = max(max_len, dp[i%2][j])

  print(dp)
  return max_len
def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))


main()
