# -*- coding: utf-8 -*-
import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root):
        if root is None:
            return None

        acc, stack, seen = 0, [root], set()
        while len(stack) > 0:
            current = stack[-1]
            if current.right is not None and (current.right not in seen):
                stack.append(current.right)
                continue
            else:
                current = stack.pop()
                seen.add(current)
                current.val = current.val + acc
                acc = current.val
                if current.left is not None and (current.left not in seen):
                    stack.append(current.left)
            # print(current.val, [node.val for node in stack], seen)
        return root


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    s.bstToGst(root)
