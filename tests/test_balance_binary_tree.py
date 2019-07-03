# -*- coding: utf-8 -*-

from balanced_binary_tree2 import Solution
from balanced_binary_tree2 import TreeNode


if __name__ == '__main__':
    s = Solution()
    result = s.bfs(None)
    assert result == 0

    tree = TreeNode(3)
    tree.left = TreeNode(3)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    result = s.bfs(tree)
    print(result)
    assert result == 3

    result = s.isBalanced(tree)
    print(result)
    assert result is True

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(3)
    tree.left.left.left = TreeNode(4)
    tree.left.left.right = TreeNode(4)
    result = s.isBalanced(tree)
    print(result)
    assert result is False

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.right.right = TreeNode(3)
    tree.left.left.left = TreeNode(4)
    tree.right.right.right = TreeNode(4)
    result = s.isBalanced(tree)
    print(result)
    assert result is False
