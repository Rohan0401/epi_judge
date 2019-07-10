
def LCS(X,Y):


    # Get the length of string
    m = len(X)
    n = len(Y)
    print(m , n)
    if m == 0 or n == 0:
        return ""
    mem = [[None]*(n+1) for i in range(m+1)]
    print(mem)
    for i in range(n+1):
        for j in range(m+1):
            if (i == 0 or j == 0):
                mem[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                mem[i][j] = mem[i-1][j-1] + 1
            else:
                mem[i][j] = max(mem[i-1][j], mem[i][j-1])
    print(mem)
    return mem[m][n]


if __name__ == '__main__':
    print(LCS("", "AGFTCR"))

