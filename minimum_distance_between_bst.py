# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def in_order(self, root):
        if root is None:
            return

        if root.left:
            for item in self.in_order(root.left):
                yield item

        yield root.val

        if root.right:
            for item in self.in_order(root.right):
                yield item

    def minDiffInBST(self, root):
        # 左 -> 中 -> 右的顺序是递增序
        prev, result = None, 101
        for current in self.in_order(root):
            if prev:
                diff = current - prev
                if diff < result:
                    result = diff
            prev = current
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    r = s.minDiffInBST(root)
    print(r)
