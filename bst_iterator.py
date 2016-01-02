__author__ = 'guang'

from bst import TreeNode

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        >>> root = TreeNode(None).from_string("#")
        >>> root is None
        True
        >>> i, v = BSTIterator(root), []
        >>> while i.hasNext(): v.append(i.next())
        >>> v
        []

        >>> root = TreeNode(None).from_string("10,2,15,1,#,12,17,#,#,#,13,16,18")
        >>> i, v = BSTIterator(root), []
        >>> while i.hasNext(): v.append(i.next())
        >>> v
        [1, 2, 10, 12, 13, 15, 16, 17, 18]
        """
        self.root = root
        self.sentinels = self._sentinels_of(self.root)

    def _sentinels_of(self, root):
        """
        >>> root = TreeNode(None).from_string("10,2,15,1,#,12,17,#,#,#,13,16,18")
        >>> nodes = BSTIterator(root).sentinels
        >>> values = [node.val for node in nodes if node]
        >>> values
        [1, 2, 10]
        """
        node = root
        result = []
        while node:
            result.append(node)
            node = node.left

        return result[::-1]

    def hasNext(self):
        """
        :rtype: bool
        >>> iterator = BSTIterator(None)
        >>> iterator.sentinels == []
        True
        >>> iterator.hasNext()
        False
        """
        if self.sentinels:
            return True

        return False

    def next(self):
        """
        :rtype: int
        """
        sentinel = self.sentinels.pop(0)
        if sentinel.right:
            new_sentinels = self._sentinels_of(sentinel.right)
            new_sentinels.extend(self.sentinels)
            self.sentinels = new_sentinels
        return sentinel.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
