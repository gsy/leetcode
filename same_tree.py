__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        >>> s = Solution()
        >>> one, another_one = TreeNode(1), TreeNode(1)
        >>> s.isSameTree(one, None)
        False
        >>> s.isSameTree(None, one)
        False
        >>> s.isSameTree(one, another_one)
        True
        """
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
