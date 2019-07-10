from test_framework import generic_test


def has_two_sum(A, t):
    # TODO - you fill in here.
    cache = {}
    for idx, val in enumerate(A):
        if not cache[t-val]:
            cache[val] = idx


    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
