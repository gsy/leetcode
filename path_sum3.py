__author__ = 'guang'

__author__ = 'guang'

from bst import TreeNode

class Solution(object):
    def is_leaf(self, node):
        return node and node.left is None and node.right is None

    def path_sum(self, node, sum, target, sub, result):
        """
        >>> s = Solution()
        >>> result = []
        >>> s.path_sum(None, 0, 10, [], result)
        >>> result
        []
        >>> result = []
        >>> s.path_sum(TreeNode(2), 0, 2, [], result)
        >>> result
        [[2]]
        >>> result = []
        >>> s.path_sum(TreeNode(2), 0, 1, [], result)
        >>> result
        []
        >>> tree = TreeNode(None).from_string("1,2,3")
        >>> result = []
        >>> s.path_sum(tree, 0, 3, [], result)
        >>> result
        [[1, 2]]
        >>> result = []
        >>> s.path_sum(tree, 0, 4, [], result)
        >>> result
        [[1, 3]]
        >>> result = []
        >>> s.path_sum(tree, 0, 1, [], result)
        >>> result
        []
        >>> result = []
        >>> tree = TreeNode(None).from_string("5,4,8,11,#,13,4,7,2,#,#,5,1")
        >>> s.path_sum(tree, 0, 22, [], result)
        >>> result
        [[5, 4, 11, 2], [5, 8, 4, 5]]
        """
        if node is None:
            return

        sub.append(node)
        if self.is_leaf(node) and sum + node.val == target:
            values = [node.val for node in sub]
            result.append(values)
            sub.pop()
            return

        self.path_sum(node.left, node.val + sum, target, sub, result)
        self.path_sum(node.right, node.val + sum, target, sub, result)
        sub.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        >>> s = Solution()
        >>> tree = TreeNode(None).from_string("5,4,8,11,#,13,4,7,2,#,#,5,1")
        >>> s.pathSum(tree, 22)
        [[5, 4, 11, 2], [5, 8, 4, 5]]
        """
        if root is None:
            return []
        result = []
        self.path_sum(root, 0, sum, [], result)
        return result

