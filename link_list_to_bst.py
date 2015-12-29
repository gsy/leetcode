__author__ = 'guang'

from linklist import LinkedList, ListNode
from bst import TreeNode, BST

class Solution(object):

    def length(self, ls):
        """
        >>> s = Solution()
        >>> ls = LinkedList.fromList([1,2,3])
        >>> s.length(ls)
        3
        """
        count = 0
        node = ls
        while node:
            count += 1
            node = node.next

        return count

    def is_leaf(self, tree):
        return tree and tree.left is None and tree.right is None

    def is_full(self, tree, count):
        """
        >>> s = Solution()
        >>> s.is_full(TreeNode(1), 1)
        True
        >>> one, two = TreeNode(1), TreeNode(2)
        >>> two.left = one
        >>> s.is_full(two, 2)
        False
        """
        n = self.height(tree)
        return count == (2 ** n) - 1

    def cons(self, x, tree, count):
        """
        >>> s = Solution()
        >>> tree = s.cons(1, None, 0)
        >>> tree.val
        1
        >>> tree = s.cons(2, tree, 1)
        >>> tree.val == 2 and tree.left.val == 1
        True
        >>> tree = s.cons(3, tree, 2)
        >>> tree.val == 2 and tree.left.val == 1 and tree.right.val == 3
        True
        """
        if tree is None:
            tree = TreeNode(x)
            return tree

        # construct subtree and append it to original tree
        n = self.height(tree)
        if self.is_full(tree, count):
            new_root = TreeNode(x)
            new_root.left = tree
            return new_root
        else:
            tree.right = self.cons(x, tree.right, count - 2 ** (n - 1))
            return tree

    def height(self, tree):
        """
        >>> s = Solution()
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> one.right, two.right = two, three
        >>> s.height(one)
        3
        >>> s.height(two)
        2
        >>> s.height(three)
        1
        """
        count = 0
        if tree is None:
            return count
        else:
            return 1 + max(self.height(tree.left), self.height(tree.right))

    def list_to_BST_helper(self, node, start, end):
        """
        >>> s = Solution()
        >>> node = LinkedList.fromList([4, 5])
        >>> tree, head = s.list_to_BST_helper(node, 4, 5)
        >>> tree.val
        5
        >>> tree.left.val
        4
        >>> head.val
        5
        >>> node = LinkedList.fromList([1, 2])
        >>> tree, head = s.list_to_BST_helper(node, 1, 2)
        >>> tree.val
        2
        >>> tree.left.val
        1
        >>> head.val
        2
        >>> node = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> tree, head = s.list_to_BST_helper(node, 1, 5)
        >>> head.val
        5

        # >>> BST(tree).show()

        >>> node = LinkedList.fromList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        >>> tree, head = s.list_to_BST_helper(node, 1, 15)
        >>> head.val
        15
        >>> BST(tree).show()


        """
        length = end - start + 1

        if length <= 0 or node is None:
            return None, node

        if length == 1:
            tree = TreeNode(node.val)
            return tree, node
        elif length == 2:
            left = TreeNode(node.val)
            node = node.next
            root = TreeNode(node.val)
            root.left = left
            return root, node
        elif length == 3:
            left = TreeNode(node.val)
            node = node.next
            root = TreeNode(node.val)
            node = node.next
            right = TreeNode(node.val)
            root.left = left
            root.right = right
            return root, node

        middle = start + length / 2
        left, head = self.list_to_BST_helper(node, start, middle - 1)
        head = head.next
        root = TreeNode(head.val)
        root.left = left
        head = head.next
        right, new_head = self.list_to_BST_helper(head, middle + 1, end)
        root.right = right
        return root, new_head

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> result = s.sortedListToBST(head)
        >>> result.val
        2
        >>> head = LinkedList.fromList([1, 2])
        >>> result = s.sortedListToBST(head)
        >>> result.val
        2
        >>> result.left.val
        1
        >>> result.right

        >>> head = LinkedList.fromList([1])
        >>> result = s.sortedListToBST(head)
        >>> result.val == 1 and result.left is None and result.right is None
        True
        """
        if head is None:
            return None

        length = self.length(head)
        return self.list_to_BST_helper(head, 1, length)[0]



