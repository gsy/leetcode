from bst import TreeNode

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("1")
        >>> s.zigzagLevelOrder(root)
        [[1]]
        >>> root = TreeNode(None).from_string("1,2")
        >>> s.zigzagLevelOrder(root)
        [[1], [2]]
        >>> root = TreeNode(None).from_string("1,#,3")
        >>> s.zigzagLevelOrder(root)
        [[1], [3]]
        >>> root = TreeNode(None).from_string("1,2,3")
        >>> s.zigzagLevelOrder(root)
        [[1], [3, 2]]
        >>> root = TreeNode(None).from_string("3,9,20,#,#,15,7")
        >>> s.zigzagLevelOrder(root)
        [[3], [20, 9], [15, 7]]
        >>> root = TreeNode(None).from_string("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16")
        >>> s.zigzagLevelOrder(root)
        [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8], [16]]
        """
        if root is None:
            return []

        levels = [[root]]
        result = [[root.val]]

        for level in levels:
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if new_level:
                levels.append(new_level)
                result.append([node.val for node in new_level])

        for height, level in enumerate(result):
            if (height + 1) % 2 == 0:
                result[height] = level[::-1]

        return result
