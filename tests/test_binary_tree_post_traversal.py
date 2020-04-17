# -*- coding: utf-8 -*-

from binary_tree_postorder_traversal import TreeNode, Solution


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    result = s.postorderTraversal(root)
    print(result)
    assert result == [3, 2, 1]
