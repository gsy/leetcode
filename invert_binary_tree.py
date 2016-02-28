from bst import TreeNode

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("6")
        >>> result = s.invertTree(root)
        >>> result.left is None and result.right is None and result.val == 6
        True
        >>> root = TreeNode(None).from_string("6,3,#")
        >>> result = s.invertTree(root)
        >>> result.val == 6 and result.left is None and result.right.val == 3
        True
        >>> root = TreeNode(None).from_string("6,3,2")
        >>> result = s.invertTree(root)
        >>> result.val == 6 and result.left.val == 2 and result.right.val == 3
        True
        """
        if root is None:
            return None

        left = root.left
        right = root.right

        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root
