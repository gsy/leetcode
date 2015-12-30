__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def height(self, node):
        """
        >>> s = Solution()
        >>> node = TreeNode(1)
        >>> s.height(node)
        1
        >>> one, two, three, four = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
        >>> one.left, one.right, three.left = two, three, four
        >>> s.height(one)
        3
        >>> s.height(two)
        1
        >>> s.height(three)
        2
        """
        if node is None:
            return 0

        return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        >>> s = Solution()
        >>> one, two, three, four = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
        >>> one.left, one.right, three.left = two, three, four
        >>> s.isBalanced(one)
        True
        >>> one, two, three, four, five = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
        >>> one.left, one.right, three.left, four.left = two, three, four, five
        >>> s.isBalanced(one)
        False
        >>> s.isBalanced(three)
        False
        """
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        difference = abs(left_height - right_height)
        if difference > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)


