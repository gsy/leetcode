__author__ = 'guang'

from linklist import LinkedList, ListNode
from bst import TreeNode, BST

class Solution(object):

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

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> result = s.sortedListToBST(head)
        >>> tree = BST(result)
        >>> tree.show()

        >>> head = LinkedList.fromList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> result = s.sortedListToBST(head)
        >>> tree = BST(result)
        >>> tree.show()
        >>> head = LinkedList

        """
        if head is None:
            return None

        node = head
        tree = None
        count = 0
        while node:
            tree = self.cons(node.val, tree, count)
            node = node.next
            count += 1

        return tree

