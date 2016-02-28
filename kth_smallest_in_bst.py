from bst import TreeNode

class Solution(object):
    def inorder_traversal(self, root):
        """
        :param root:
        :return:
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("6,2,8,0,4,7,9,#,#,3,5")
        >>> result = [node.val for node in s.inorder_traversal(root)]
        >>> result
        [0, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        if root is None:
            return []

        return self.inorder_traversal(root.left) + [root] + self.inorder_traversal(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("6,2,8,0,4,7,9,#,#,3,5")
        >>> s.kthSmallest(root, 1)
        0
        >>> s.kthSmallest(root, 2)
        2
        """
        if root is None:
            return None

        nodes = self.inorder_traversal(root)
        return nodes[k - 1].val
