def find_happy_number(num):
    # A happy number is the one which having the cycle

    # Finding a cycle in LinkedList

    # Two pointers slow and Fast and if they intersect somewhere we have the cycle
    slow, fast = num, num

    while True:
        slow, fast = find_sum_of_square(slow), find_sum_of_square(find_sum_of_square(fast))

        if slow == fast: #found cycle
            break


    return slow == 1

def find_sum_of_square(num):
    _sum = 0

    while num > 0:
        digit = num % 10
        _sum += digit*digit
        num = num // 10

    return _sum

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
