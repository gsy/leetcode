__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def is_leaf(self, node):
        return node and node.left is None and node.right is None

    def deep_fisrt_search(self, node, sum_tag):
        """
        >>> s = Solution()
        >>> node = TreeNode(1)
        >>> s.deep_fisrt_search(node, 0)
        1
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> one.left, one.right = two, three
        >>> s.deep_fisrt_search(two, 1)
        12
        >>> s.deep_fisrt_search(three, 1)
        13
        >>> one, two, three, four, five = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
        >>> one.left, two.left, three.left = two, three, four
        >>> two.right = five
        >>> s.deep_fisrt_search(one, 0)
        1359
        """
        if node is None:
            return 0

        if self.is_leaf(node):
            return sum_tag * 10 + node.val

        new_tag = sum_tag * 10 + node.val
        result = 0
        if node.left:
            result += self.deep_fisrt_search(node.left, new_tag)
        if node.right:
            result += self.deep_fisrt_search(node.right, new_tag)
        return result

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return self.deep_fisrt_search(root, 0)




