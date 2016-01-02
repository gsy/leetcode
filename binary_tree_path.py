__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def is_leaf(self, node):
        return node and node.left is None and node.right is None

    def dfs(self, node):
        """
        >>> s = Solution()
        >>> s.dfs(None)
        []
        >>> s.dfs(TreeNode(4))
        [[4]]
        >>> tree = TreeNode(None).from_string("1,2,3")
        >>> s.dfs(tree)
        [[1, 2], [1, 3]]
        >>> tree = TreeNode(None).from_string("1,2,3,4,5")
        >>> s.dfs(tree)
        [[1, 2, 4], [1, 2, 5], [1, 3]]
        """
        if node is None:
            return []

        if self.is_leaf(node):
            return [[str(node.val)]]

        result = []
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        for sub in left:
            tmp = [str(node.val)]
            tmp.extend(sub)
            result.append(tmp)

        for sub in right:
            tmp = [str(node.val)]
            tmp.extend(sub)
            result.append(tmp)

        return result

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        >>> s = Solution()
        >>> s.binaryTreePaths(None)
        []
        >>> s.binaryTreePaths(TreeNode(4))
        ['4']
        >>> tree = TreeNode(None).from_string("1,2,3")
        >>> s.binaryTreePaths(tree)
        ['1->2', '1->3']
        >>> tree = TreeNode(None).from_string("1,2,3,4,5")
        >>> s.binaryTreePaths(tree)
        ['1->2->4', '1->2->5', '1->3']
        """
        if root is None:
            return []

        result = []
        paths = self.dfs(root)
        for path in paths:
            result.append("->".join(path))
        return result

