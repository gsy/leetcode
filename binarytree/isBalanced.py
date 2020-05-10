#!/usr/bin/env python3

class Solution:
    def recursive(self, node):
        if node is None:
            return True, 0

        left, left_height = self.recursive(node.left)
        if left is False:
            return False, 0

        right, right_height = self.recursive(node.right)

        if right is False:
            return False, 0

        if abs(left_height - right_height) <= 1:
            return True, 1 + max(left_height, right_height)

        return False, 0

    def isBalanced(self, root):
        if root is None:
            return True

        result, _ = self.recursive(root)
        return result
