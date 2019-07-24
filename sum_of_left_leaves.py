# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_leaf(self, node):
        if node is None:
            return False
        return node.left is None and node.right is None

    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0

        # breadth first search
        nodes, result = [root], 0
        while len(nodes) > 0:
            current = nodes.pop(0)
            if current.left:
                if self.is_leaf(current.left):
                    result = result + current.left.val
                else:
                    nodes.append(current.left)
            if current.right:
                nodes.append(current.right)
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    r = s.sumOfLeftLeaves(root)
    print(r)
    assert r == (9 + 15)
