__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        >>> s = Solution()
        >>> s.postorderTraversal(None)
        []
        >>> s.postorderTraversal(TreeNode(2))
        [2]
        >>> tree = TreeNode(None).from_string("1,2,3")
        >>> s.postorderTraversal(tree)
        [2, 3, 1]
        >>> tree = TreeNode(None).from_string("1,#,2,3")
        >>> s.postorderTraversal(tree)
        [3, 2, 1]
        """
        if root is None:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        result = []
        result.extend(left)
        result.extend(right)
        result.append(root.val)

        return result
