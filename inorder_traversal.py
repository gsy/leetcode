__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        >>> s = Solution()
        >>> tree = TreeNode(None).from_string("1,#,2,3")
        >>> s.inorderTraversal(tree)
        [1, 3, 2]
        >>> tree = TreeNode(None).from_string("#")
        >>> s.inorderTraversal(tree)
        []
        >>> tree = TreeNode(None).from_string("1,2,#,3,#,4,#,5")
        >>> s.inorderTraversal(tree)
        [5, 4, 3, 2, 1]
        >>> tree = TreeNode(None).from_string("1,2,3,4,#,4,5")
        >>> s.inorderTraversal(tree)
        [4, 2, 1, 4, 3, 5]
        """
        if root is None:
            return []

        seen = []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node in seen or (node.left is None and node.right is None):
                result.append(node.val)
            else:
                if node.right and node.left:
                    stack.append(node.right)
                    stack.append(node)
                    stack.append(node.left)
                elif node.right:
                    stack.append(node.right)
                    stack.append(node)
                elif node.left:
                    stack.append(node)
                    stack.append(node.left)

                seen.append(node)

        return result
