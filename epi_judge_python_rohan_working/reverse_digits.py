from test_framework import generic_test


def reverse(x):
    # TODO - you fill in here.

    """

    APPROCH : This problem required to think in modular assignment basis also it is imporatant to know that this
    problem requires to take care about the absolute value which should not be passed in the while loop

    DATE : May 30
    :param x:
    :return:
    """
    if x < 0 :
        carry = -1
    else:
        carry = 1
    x = abs(x)
    res = 0
    while x :
        digit = x % 10
        res = res*10 + digit
        x //= 10


    return res*carry


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
