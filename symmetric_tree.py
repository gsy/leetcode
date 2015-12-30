__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def is_mirror(self, tree_a, tree_b):
        """
        >>> s = Solution()
        >>> two, three, four = TreeNode(2), TreeNode(3), TreeNode(4)
        >>> two.left, two.right = three, four
        >>> another_two, another_three, another_four = TreeNode(2), TreeNode(3), TreeNode(4)
        >>> another_two.left, another_two.right = another_four, another_three
        >>> s.is_mirror(three, another_three)
        True
        >>> s.is_mirror(two, another_two)
        True
        """
        if tree_a is None and tree_b is None:
            return True
        elif tree_a is None:
            return False
        elif tree_b is None:
            return False
        else:
            if tree_a.val != tree_b.val:
                return False
            else:
                return self.is_mirror(tree_a.left, tree_b.right) and self.is_mirror(tree_a.right, tree_b.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        >>> s = Solution()
        >>> root, one = TreeNode(2), TreeNode(1)
        >>> root.left = one
        >>> s.isSymmetric(root)
        False
        >>> root.right = TreeNode(1)
        >>> s.isSymmetric(root)
        True
        """
        if root is None:
            return True

        return self.is_mirror(root.left, root.right)


