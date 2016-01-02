__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def is_leaf(self, node):
        return node and node.left is None and node.right is None

    def path_sum(self, node, sum, target):
        """
        >>> s = Solution()
        >>> s.path_sum(None, 0, 10)
        False
        >>> s.path_sum(TreeNode(2), 0, 2)
        True
        >>> s.path_sum(TreeNode(2), 0, 1)
        False
        >>> tree = TreeNode(None).from_string("1,2,3")
        >>> s.path_sum(tree, 0, 3)
        True
        >>> s.path_sum(tree, 0, 4)
        True
        >>> s.path_sum(tree, 0, 1)
        False
        >>> tree = TreeNode(None).from_string("5,4,8,11,#,13,4,7,2,#,#,#,1")
        >>> s.path_sum(tree, 0, 22)
        True
        """
        if node is None:
            return False

        if self.is_leaf(node):
            return sum + node.val == target

        if self.path_sum(node.left, node.val + sum, target):
            return True
        else:
            return self.path_sum(node.right, node.val + sum, target)

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        return self.path_sum(root, 0, sum)



