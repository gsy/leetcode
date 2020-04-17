# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 深度优先搜索，找到左右子树的深度
    def bfs(self, node):
        if node is None:
            return 0

        height = 0
        level = [None, node]
        while len(level) > 0:
            node = level.pop()
            if node is None:
                height = height + 1
                if len(level) == 0:
                    break
                else:
                    level.insert(0, None)
            else:
                if node.left:
                    level.insert(0, node.left)
                if node.right:
                    level.insert(0, node.right)
        return height

    def isBalanced(self, root):
        if root is None:
            return True

        left_depth = self.bfs(root.left)
        right_depth = self.bfs(root.right)
        # print(f"left {left_depth}, right {right_depth}")
        return abs(left_depth - right_depth) <= 1
