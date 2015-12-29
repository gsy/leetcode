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

