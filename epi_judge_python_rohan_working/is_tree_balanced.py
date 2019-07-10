from test_framework import generic_test

from collections import namedtuple
def is_balanced_binary_tree(tree):
    # TODO - you fill in here

    def traverse(root, balanced):

        if root is None:
            return 0

        left = traverse(root.left, balanced)
        right = traverse(root.right, balanced)

        if abs(left - right) > 1:
            balanced = False
            return balanced
        return max(left, right) + 1
    balanced = True
    balanced = traverse(tree, balanced)
    return balanced



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
