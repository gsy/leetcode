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

        result = []
        path = [root]

        while path:
            node = path.pop(-1)
            if node.right:
                path.append(node.right)
            if node.left:
                path.append(node.left)
            result.append(node.val)

        return result
