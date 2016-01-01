__author__ = 'guang'

from bst import TreeNode

class Codec:
    def is_leaf(self, node):
        return node and node.left is None and node.right is None

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        >>> codec = Codec()
        >>> root = TreeNode(3)
        >>> one = TreeNode(1)
        >>> root.right = one
        >>> string = codec.serialize(root)
        >>> string
        '3,#,1'
        >>> one, two, three, four, five, six = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
        >>> one.left, one.right = two, three
        >>> two.left, three.right = four, five
        >>> four.right = six
        >>> codec.serialize(one)
        '1,2,3,4,#,#,5,#,6'
        >>> codec.serialize(six)
        '6'
        >>> codec.serialize(None)
        '#'
        >>> one, negative_one, two, three = TreeNode(1), TreeNode(-1), TreeNode(2), TreeNode(3)
        >>> one.left, one.right = negative_one, two
        >>> two.left = three
        >>> codec.serialize(one)
        '1,-1,2,#,#,3'
        """
        if root is None:
            return "#"

        nodes = [root]
        for node in nodes:
            if node:
                nodes.append(node.left)
                nodes.append(node.right)

        values = [str(node.val) if node else "#" for node in nodes]
        result = ','.join(values)
        result = result.rstrip(',#')
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        >>> codec = Codec()
        >>> codec.deserialize("")

        >>> tree = codec.deserialize("1")
        >>> tree.val
        1
        >>> tree = codec.deserialize("1,#,3")
        >>> tree.val
        1
        >>> tree.left is None
        True
        >>> tree.right.val
        3
        >>> tree = codec.deserialize("#")
        >>> tree is None
        True

        >>> tree = codec.deserialize("1,2,#,3,#,4,#,5")
        >>> tree.show()

        >>> tree = codec.deserialize("5,2,3,#,#,2,4,3,1")
        >>> tree.show()

        >>> tree = codec.deserialize("1,2,3,4,5")
        >>> tree.show()

        """
        if not data:
            return None

        values = data.split(',')
        nodes = [TreeNode(int(value)) if value != '#' else None for value in values]

        i, j, length = 0, 1, len(nodes)

        while j < length:
            root = nodes[i]
            if root is None:
                i += 1
                continue
            else:
                left = nodes[j]
                right = nodes[j + 1] if j + 1 < length else None
                root.left = left
                root.right = right
                i += 1
                j += 2

        return nodes[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
