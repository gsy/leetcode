__author__ = 'guang'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def show(self):
        """
        >>> one, two, three, four, five = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
        >>> three.left, two.left, three.right, four.right = two, one, four, five
        >>> three.show()
        """
        def show_node(node, k):
            if node is None:
                return

            print node.val
            if node.left:
                print "\t"*k, "left:",
            show_node(node.left, k + 1)
            if node.right:
                print "\t"*k, "right:",
            show_node(node.right, k + 1)
        show_node(self, 0)

    def from_string(self, data):
        """
        >>> codec = TreeNode(None)
        >>> codec.from_string("")

        >>> tree = codec.from_string("1")
        >>> tree.val
        1
        >>> tree = codec.from_string("1,#,3")
        >>> tree.val
        1
        >>> tree.left is None
        True
        >>> tree.right.val
        3
        >>> tree = codec.from_string("#")
        >>> tree is None
        True
        >>> tree = codec.from_string("1,2,#,3,#,4,#,5")
        >>> tree.show()

        >>> tree = codec.from_string("5,2,3,#,#,2,4,3,1")
        >>> tree.show()

        >>> tree = codec.from_string("1,2,3,4,5")
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


class BST(object):
    def __init__(self, root):
        self.root = root

    def show(self):
        """
        >>> one, two, three, four, five = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
        >>> three.left, two.left, three.right, four.right = two, one, four, five
        >>> tree = BST(three)
        >>> tree.show()
        """
        def show_node(node, k):
            if node is None:
                return

            print node.val
            if node.left:
                print "\t"*k, "left:",
            show_node(node.left, k + 1)
            if node.right:
                print "\t"*k, "right:",
            show_node(node.right, k + 1)
        show_node(self.root, 0)



