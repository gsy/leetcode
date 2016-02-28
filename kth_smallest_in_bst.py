from bst import TreeNode

class Solution(object):
    def inorder_traversal(self, root):
        """
        :param root:
        :return:
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("6,2,8,0,4,7,9,#,#,3,5")
        """
        if root is None:
            yield None

        if root.left:
            for node in self.inorder_traversal(root.left):
                yield node

        yield root

        if root.right:
            for node in self.inorder_traversal(root.right):
                yield node

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
        >>> s.kthSmallest(root, 3)
        3
        """
        if root is None:
            return None

        nodes = self.inorder_traversal(root)
        node = None

        for i in range(k):
            node = nodes.next()

        return node.val if node else None

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(None).from_string("6,2,8,0,4,7,9,#,#,3,5")
    nodes = s.inorder_traversal(root)
    print type(nodes)
    for i in range(3):
        node = nodes.next()
        print node.val

