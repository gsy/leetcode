__author__ = 'guang'

from bst import TreeNode

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



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
