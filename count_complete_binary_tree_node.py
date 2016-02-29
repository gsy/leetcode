from bst import TreeNode

class Solution(object):
    def left_most_height(self, root):
        if root is None:
            return None

        node = root
        count = 1
        while node.left:
            node = node.left
            count += 1

        return count

    def right_most_height(self, root):
        if root is None:
            return None

        node = root
        count = 1
        while node.right:
            node = node.right
            count += 1

        return count

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("2,3,4")
        >>> s.countNodes(root)
        3
        >>> root = TreeNode(None).from_string("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16")
        >>> s.countNodes(root)
        16
        >>> root = TreeNode(None).from_string("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15")
        >>> s.countNodes(root)
        15
        """
        if root is None:
            return 0

        left_height = self.left_most_height(root)
        right_height = self.right_most_height(root)

        if left_height == right_height:
            return 2 ** left_height - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

