__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def is_leaf(self, node):
        return node and node.left is None and node.right is None

    def right_most(self, node):
        """
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("2")
        >>> s.right_most(root).val
        2
        >>> root = TreeNode(None).from_string("2,#,3,#,4")
        >>> s.right_most(root).val
        4
        """
        if node is None:
            return None

        result = node
        while result.right:
            result = result.right

        return result

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("2")
        >>> s.flatten(root)
        >>> root.left is None and root.right is None and root.val == 2
        True
        >>> root = TreeNode(None).from_string("2,3")
        >>> s.flatten(root)
        >>> root.val == 2 and root.right.val == 3 and root.left is None
        True
        >>> root = TreeNode(None).from_string("2,#,4")
        >>> s.flatten(root)
        >>> root.val == 2 and root.right.val == 4 and root.left is None
        True
        >>> root = TreeNode(None).from_string("2,3,4")
        >>> s.flatten(root)
        >>> root.right.val == 3 and root.right.right.val == 4
        True
        >>> root = TreeNode(None).from_string("1,2,5,3,4,#,6")
        >>> s.flatten(root)
        >>> root.show()
        True
        """
        if root is None or self.is_leaf(root):
            return
        elif root.right is None:
            self.flatten(root.left)
            root.right = root.left
            root.left = None
        elif root.left is None:
            self.flatten(root.right)
        else:
            self.flatten(root.left)
            self.flatten(root.right)
            right_most = self.right_most(root.left)

            right_most.right = root.right
            root.right = root.left
            root.left = None
