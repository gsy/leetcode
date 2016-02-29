from bst import TreeNode

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("1")
        >>> s.rightSideView(root)
        [1]
        >>> root = TreeNode(None).from_string("1,2")
        >>> s.rightSideView(root)
        [1, 2]
        >>> root = TreeNode(None).from_string("1,2,3")
        >>> s.rightSideView(root)
        [1, 3]
        >>> root = TreeNode(None).from_string("1,2,3,#,5,#,4")
        >>> s.rightSideView(root)
        [1, 3, 4]
        >>> root = TreeNode(None).from_string("1,2,3,4")
        >>> s.rightSideView(root)
        [1, 3, 4]
        >>> root = TreeNode(None).from_string("1,2,3,4,#,#,5")
        >>> s.rightSideView(root)
        [1, 3, 5]
        """
        if root is None:
            return []

        level = [root]
        result = []

        while level:
            node = level[-1]
            result.append(node.val)
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level = new_level

        return result
