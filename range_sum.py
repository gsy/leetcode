# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        if root is None:
            return 0

        if root.val < L:
            return self.rangeSumBST(root.right, L, R)

        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return self.rangeSumBST(root.left, L, R) + root.val + self.rangeSumBST(root.right, L, R)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    r = s.rangeSumBST(root, 7, 15)
    print(r)
    assert r == 32
