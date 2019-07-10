from test_framework import generic_test

result = []

def inorder_traversal(tree):
    # TODO - you fill in here.
    if not tree:
        return
    inorder_traversal(tree.left)
    result.append(tree.data)
    inorder_traversal(tree.right)

    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))

