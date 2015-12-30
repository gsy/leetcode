__author__ = 'guang'

__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def is_leaf(self, node):
        return node and node.left is None and node.right is None

    def min_depth(self, a, b):
        if a is None and b is None:
            return 0
        elif a is None:
            return b
        elif b is None:
            return a
        else:
            return min(a, b)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        >>> s = Solution()
        >>> one = TreeNode(1)
        >>> s.minDepth(one)
        1
        >>> one, two, three, four = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
        >>> one.left, one.right, three.left = two, three, four
        >>> s.minDepth(one)
        2
        >>> s.minDepth(two)
        1
        >>> s.minDepth(three)
        2
        >>> s.minDepth(four)
        1
        """
        if root is None:
            return 0

        if self.is_leaf(root):
            return 1

        min_left, min_right = None, None
        if root.left:
            min_left = self.minDepth(root.left)
        if root.right:
            min_right = self.minDepth(root.right)

        return 1 + self.min_depth(min_left, min_right)


