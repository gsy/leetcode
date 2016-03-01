class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

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
            if node.next:
                print "\t"*k, "next:",
            show_node(node.next, k + 1)
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

class Solution(object):
    def closest_cousin(self, parent):
        node = parent.next
        while node:
            if node.left:
                return node.left
            elif node.right:
                return node.right
            else:
                node = node.next

        return None

    def left_next(self, parent):
        if parent.right:
            return parent.right

        return self.closest_cousin(parent)

    def right_next(self, parent):
        return self.closest_cousin(parent)

    def new_head(self, node):
        while node:
            if node.left or node.right:
                return node.left if node.left else node.right
            else:
                node = node.next
        return None

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        >>> s = Solution()
        >>> root = TreeNode(None).from_string("1,2,3,4,5,6,7")
        >>> s.connect(root)
        >>> root.show()

        >>> root = TreeNode(None).from_string("0,2,4,1,#,3,-1,5,1,#,6,#,8")
        >>> s.connect(root)
        >>> root.show()
        """
        if root is None:
            return

        head = root
        while head:
            parent = head
            while parent:
                if parent.left:
                    parent.left.next = self.left_next(parent)
                if parent.right:
                    parent.right.next = self.right_next(parent)
                parent = parent.next
            head = self.new_head(head)
