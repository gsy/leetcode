# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_height(self, root):
        if root is None:
            return 0

        result = 1
        while root.left:
            result = result + 1
            root = root.left
        return result

    def full(self, root, height):
        if height in (0, 1):
            return True

        right_most = 0
        while root.right:
            right_most = right_most + 1
            root = root.right

        return right_most == height

    def countNodes(self, root):
        if root is None:
            return 0

        height = self.get_height(root)
        if self.full(root, height):
            return 2 ** height - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == '__main__':
    s = Solution()
    tree = None
    r = s.countNodes(tree)
    assert r == 0

    tree = TreeNode(1)
    r = s.countNodes(tree)
    print(r)
    assert r == 1

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    r = s.countNodes(tree)
    assert r == 2

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    r = s.countNodes(tree)
    assert r == 3

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    r = s.countNodes(tree)
    assert r == 7

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    r = s.countNodes(tree)
    assert r == 6

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    r = s.countNodes(tree)
    assert r == 5

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    r = s.countNodes(tree)
    assert r == 4
