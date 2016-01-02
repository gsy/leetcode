__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def is_leaf(self, node):
        return node and node.left is None and node.right is None

    def path_sum(self, node):
        """
        >>> s = Solution()
        >>> s.path_sum(None)
        (0, -2147483648)
        >>> s.path_sum(TreeNode(2))
        (2, 2)
        >>> s.path_sum(TreeNode(-2))
        (-2, -2)
        >>> tree = TreeNode(None).from_string("1,2,3")
        >>> s.path_sum(tree.left)
        (2, 2)
        >>> s.path_sum(tree.right)
        (3, 3)
        >>> tree = TreeNode(None).from_string("5,1,-10,2,3,-5,-6")
        >>> s.path_sum(tree.left)
        (4, 6)
        >>> s.path_sum(tree.right)
        (-10, -5)
        >>> tree = TreeNode(None).from_string("-10,-5,-6,-3,-7,-8,-9")
        >>> s.path_sum(tree)
        (-10, -3)
        >>> tree = TreeNode(None).from_string("-2,-1")
        >>> s.path_sum(tree)
        (-2, -1)
        >>> tree = TreeNode(None).from_string("5,4,8,11,#,13,4,7,2,#,#,#,1")
        >>> s.path_sum(tree.left)
        (22, 22)
        >>> s.path_sum(tree.right)
        (21, 26)
        >>> tree = TreeNode(None).from_string("7,-2000,#,500,#,1500,2000")
        >>> s.path_sum(tree.left.left)
        (2500, 4000)
        """
        if self.is_leaf(node):
            return node.val, node.val
        if node is None:
            return 0, -2147483648

        left, sub1 = self.path_sum(node.left)
        right, sub2 = self.path_sum(node.right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0

        if left > right:
            maximum_path = node.val + left
        else:
            maximum_path = node.val + right

        sub_result = max(max(sub1, sub2), node.val + left + right)
        return maximum_path, sub_result

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        >>> s = Solution()
        >>> s.maxPathSum(None)
        0
        >>> s.maxPathSum(TreeNode(2))
        2
        >>> s.maxPathSum(TreeNode(-2))
        -2
        >>> s.maxPathSum(TreeNode(None).from_string("2,-1"))
        2
        >>> s.maxPathSum(TreeNode(None).from_string("1,2,#"))
        3
        >>> s.maxPathSum(TreeNode(None).from_string("1,2,3"))
        6
        >>> s.maxPathSum(TreeNode(None).from_string("5,1,-10,2,3,-5,-6"))
        9
        >>> s.maxPathSum(TreeNode(None).from_string("5,4,8,11,#,13,4,7,2,#,#,#,1"))
        48
        >>> s.maxPathSum(TreeNode(None).from_string("-10,-5,-6,-3,-7,-8,-9"))
        -3
        >>> s.maxPathSum(TreeNode(None).from_string("-5,7,#,8,9"))
        24
        >>> tree = TreeNode(None).from_string("7,-2000,#,500,#,1500,2000")
        >>> s.maxPathSum(tree)
        4000
        """
        if root is None:
            return 0

        left, left_max = self.path_sum(root.left)
        right, right_max = self.path_sum(root.right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        return max(root.val + left + right, max(left_max, right_max))
