# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        # 广度优先
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            stack1, stack2 = [p], [q]

            while len(stack1) > 0 or len(stack2) > 0:
                node1 = stack1.pop()
                node2 = stack2.pop()
                if node1.val != node2.val:
                    return False
                if (node1.left is None and node2.left is not None) or \
                   (node1.left is not None and node2.left is None):
                    return False

                if (node1.right is None and node2.right is not None) or \
                   (node1.right is not None and node2.right is None):
                    return False

                if node1.left is not None:
                    stack1.append(node1.left)
                if node1.right is not None:
                    stack1.append(node1.right)

                if node2.left is not None:
                    stack2.append(node2.left)
                if node2.right is not None:
                    stack2.append(node2.right)
            return len(stack1) == len(stack2)


if __name__ == "__main__":
    s = Solution()
    left = TreeNode(1)
    left.left = TreeNode(2)
    left.right = TreeNode(3)
    right = TreeNode(1)
    right.left = TreeNode(2)
    right.right = TreeNode(3)
    r = s.isSameTree(left, right)
    assert r is True

    left = TreeNode(1)
    left.left = TreeNode(2)
    right = TreeNode(1)
    right.right = TreeNode(3)
    r = s.isSameTree(left, right)
    assert r is False

    left = TreeNode(1)
    left.left = TreeNode(2)
    left.right = TreeNode(1)
    right = TreeNode(1)
    right.left = TreeNode(1)
    right.right = TreeNode(2)
    r = s.isSameTree(left, right)
    assert r is False
