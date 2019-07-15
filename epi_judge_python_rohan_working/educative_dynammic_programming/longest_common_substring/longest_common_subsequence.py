def find_LCS_length(s1, s2):
  m, n = len(s1), len(s2)
  if m <= 0 or n <= 0:
     return 0
  dp = [[0 for x in range(n+1)] for y in range(m+1)]
  max_len = 0
  for i in range(1, m+1):
    for j in range(1, n+1):
      if s1[i-1] == s2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
          dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      max_len = max(max_len, dp[i][j])

  # printitng LCS
  index = dp[m][n]

  # create an chear array for printing the string
  lcs = [""] * (index)
  print(lcs)
  #lcs[index] = ""

  # start from right most corner
  i = m
  j = n

  while i > 0 and j > 0:
    # if current s1 and s2 are same then they are part of lcs
    if s1[i-1] == s2[j-1]:
      lcs[index-1] = s1[i-1]
      i -= 1
      j -= 1
      index -= 1

    # if not then find the larger of two and go in that direction
    elif dp[i-1][j] > dp[i][j-1]:
      i -= 1
    else:
      j -= 1

  print("".join(lcs))



  return max_len






def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))


main()
