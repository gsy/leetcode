# -*- coding: utf-8 -*-

from binary_tree_inorder_traversal import Solution


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    s = Solution()
    r = s.inorderTraversal(None)
    print(r)
    assert r == []

    tree = TreeNode(1)
    tree.left = None
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    r = s.inorderTraversal(tree)
    print(r)
    assert r == [1, 3, 2]
