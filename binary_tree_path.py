__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def is_leaf(self, node):
        return node and node.left is None and node.right is None

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

        paths = []
        stack = [root]
        seen = []
        while stack:
            node = stack[-1]
            if node.left and node.left not in seen:
                stack.append(node.left)
            elif node.right and node.right not in seen:
                stack.append(node.right)
            else:
                if self.is_leaf(node):
                    paths.append(stack[::])
                seen.append(stack.pop())

        result = []
        for path in paths:
            values = [str(node.val) for node in path]
            result.append("->".join(values))

        return result

