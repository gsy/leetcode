__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        >>> s = Solution()
        >>> one = TreeNode(1)
        >>> s.maxDepth(one)
        1
        >>> one, two, three, four = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
        >>> one.left, one.right, three.left = two, three, four
        >>> s.maxDepth(one)
        3
        >>> s.maxDepth(two)
        1
        >>> s.maxDepth(three)
        2
        """
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
