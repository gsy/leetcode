from bst import TreeNode

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("1,2,3")
        >>> s.preorderTraversal(root)
        [1, 2, 3]
        >>> root = TreeNode(None).from_string("1,2")
        >>> s.preorderTraversal(root)
        [1, 2]
        >>> root = TreeNode(None).from_string("1,#,3")
        >>> s.preorderTraversal(root)
        [1, 3]
        >>> root = TreeNode(None).from_string("1,2,3,4,5,6,7")
        >>> s.preorderTraversal(root)
        [1, 2, 4, 5, 3, 6, 7]
        """
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
