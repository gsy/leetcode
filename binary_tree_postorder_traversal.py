# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []

        result = []

        if root.left is not None:
            result.extend(self.postorderTraversal(root.left))

        if root.right is not None:
            result.extend(self.postorderTraversal(root.right))

        result.append(root.val)

        return result
