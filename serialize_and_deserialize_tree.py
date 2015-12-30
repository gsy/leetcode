__author__ = 'guang'

from bst import TreeNode
try:
    import cPickle as pickle
except:
    import pickle


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        >>> codec = Codec()
        >>> root = TreeNode(3)
        >>> one = TreeNode(1)
        >>> root.left = one
        >>> string = codec.serialize(root)
        >>> tree = codec.deserialize(string)
        >>> tree.val
        3
        >>> tree.left.val
        1
        """
        return pickle.dumps(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return pickle.loads(data)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
