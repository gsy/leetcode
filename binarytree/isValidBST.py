#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, node):
        if node is None:
            return True, None, None

        left_valid, l1, r1 = self.check(node.left)
        if left_valid is False:
            return False, None, None

        right_valid, l2, r2 = self.check(node.right)
        if right_valid is False:
            return False, None, None

        if (r1 is not None and node.val <= r1) or (l2 is not None and node.val >= l2):
            return False, None, None

        return True, (l1 or node.val), (r2 or node.val)


    def isValidBST(self, root):
        result, _, _ = self.check(root)
        return result
