__author__ = 'guang'

__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        >>> s = Solution()
        >>> three, nine, twenty, fifty, seven = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
        >>> three.left, three.right, twenty.left, twenty.right = nine, twenty, fifty, seven
        >>> result = s.levelOrderBottom(three)
        >>> result
        [[15, 7], [9, 20], [3]]
        >>> one = TreeNode(1)
        >>> s.levelOrderBottom(one)
        [[1]]
        """
        if root is None:
            return []

        result = []
        parents = [root]
        while parents:
            nodes = []
            values = []
            for parent in parents:
                values.append(parent.val)
                if parent.left:
                    nodes.append(parent.left)
                if parent.right:
                    nodes.append(parent.right)
            parents = nodes
            result.append(values)

        return result[::-1]


