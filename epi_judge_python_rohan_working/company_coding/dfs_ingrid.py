import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
def maxRegion(grid):
    # Start with the base case

    if len(grid) <= 0 and len(grid[0]) <= 0:
        return -1

    def isSafe(grid, row, col, visited):
        """row in range, col in range, value is one and not visited"""
        global ROW, COL

        return ((row >= 0 and row < ROW) and
               (col >= 0 and col < COL) and
               grid[row][col] and (row, col) not in visited)
    def dfs(grid: List[List], row: object, col: object, count: object, visited: object) -> object:
        """Apply DFS for the grid cell"""
        rowIDX = [-1, -1, -1, 0, 1, 1, 1, 0]
        colIDX = [-1, 0, 1, 1, 1, 0, -1, -1]
        visited.add((row, col))
        for k in range(8):
            if isSafe(grid, row + rowIDX[k], col+colIDX[k],visited):
                count[0] += 1
                dfs(grid, row + rowIDX[k], col+colIDX[k],count, visited)

    global ROW, COL
    ROW, COL = len(grid), len(grid[0])
    # Track visited
    visited = set()
    result = -1
    for row in range(ROW):
        for col in range(COL):
            if isSafe(grid, row, col,visited):
                count = [1]
                dfs(grid, row, col, count, visited)
                # max region
                result = max(result, count[0])

    return result












if __name__ == '__main__':
 #   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))



    res = maxRegion(grid)
    print(res)
    print(grid)

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
