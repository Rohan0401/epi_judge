def find_max_water(height):
    if not height:
        return 0
    leftMax, rightMax, ans, left, right = 0, 0 , 0, 0, len(height) - 1
    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                ans += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                ans +=rightMax - height[right]
            right -=1
    return ans

def main():
  print(find_max_water([0,1,0,2,1,0,1,3,2,1,2,1]))
  print(find_max_water([3, 2, 5, 4, 2]))
  print(find_max_water([1, 4, 3, 2, 5, 8, 4]))


main()
