__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def right_most(self, node):
        """
        >>> s = Solution()
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> two.left, one.right = one, three
        >>> result = s.right_most(one)
        >>> result.val
        3
        >>> result = s.right_most(two)
        >>> result.val
        2
        """
        if node is None:
            return None

        while node.right:
            node = node.right
        return node

    def left_most(self, node):
        """
        >>> s = Solution()
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> two.left, one.right = one, three
        >>> result = s.left_most(one)
        >>> result.val
        1
        >>> result = s.left_most(two)
        >>> result.val
        1
        """
        if node is None:
            return None

        while node.left:
            node = node.left

        return node

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        >>> s = Solution()
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> two.left, two.right = one, three
        >>> root = two
        >>> s.isValidBST(root)
        True
        >>> s.isValidBST(one)
        True
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> two.left, one.right = one, three
        >>> root = two
        >>> s.isValidBST(root)
        False
        """
        if root is None:
            return True

        result = False
        if self.isValidBST(root.left) and self.isValidBST(root.right):
            max_left = self.right_most(root.left)
            min_right = self.left_most(root.right)
            if max_left and min_right:
                result = max_left.val < root.val < min_right.val
            elif max_left:
                result = max_left.val < root.val
            elif min_right:
                result = root.val < min_right.val
            else:
                result = True

        return result


