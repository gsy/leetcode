__author__ = 'guang'

from linklist import LinkedList, ListNode
from bst import TreeNode, BST

class Solution(object):
    def find_parent(self, x, root):
        """
        >>> s = Solution()
        >>> root = TreeNode(1)
        >>> two = TreeNode(2)
        >>> three = TreeNode(3)
        >>> root.right = two
        >>> two.right = three
        >>> p = s.find_parent(0, root)
        >>> p.val
        1
        >>> p = s.find_parent(4, root)
        >>> p.val
        3
        """
        if root is None:
            return None

        p = root
        while p:
            if x < p.val:
                if p.left:
                    p = p.left
                else:
                    return p
            else:
                if p.right:
                    p = p.right
                else:
                    return p

    def cons(self, x, tree):
        """
        >>> s = Solution()
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> one.right, two.right = two, three
        >>> result = s.cons(4, one)
        >>> three.right.val
        4
        >>> tree = one
        >>> result = s.cons(0, tree)
        >>> one.left.val
        0
        """
        # construct a new BST

        if tree is None:
            tree = TreeNode(x)
            return tree
        # construct subtree and append it to original tree
        node = TreeNode(x)
        p = self.find_parent(x, tree)
        if x < p.val:
            p.left = node
        else:
            p.right = node
        return tree

    def is_leaf(self, tree):
        return tree is None or (tree.left is None and tree.right is None)

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

    def is_balance(self, tree):
        """
        >>> s = Solution()
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> one.right, two.right = two, three
        >>> s.is_balance(one)
        False
        >>> s.is_balance(two)
        True
        >>> s.is_balance(three)
        True
        >>> one, two, three, four, five, six = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
        >>> four.left, three.left, two.left = three, two, one
        >>> four.right, five.right = five, six
        >>> s.is_balance(four)
        False
        """
        if tree is None:
            return True

        left_height = self.height(tree.left)
        right_height = self.height(tree.right)
        return abs(left_height - right_height) <= 1 and self.is_balance(tree.left) and self.is_balance(tree.right)

    def rebalance(self, tree):
        """
        >>> s = Solution()
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> one.right, two.right = two, three
        >>> tree = s.rebalance(one)
        >>> tree.val
        2
        >>> tree.left.val
        1
        >>> tree.right.val
        3
        >>> one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
        >>> three.left, two.left = two, one
        >>> result = s.rebalance(three)
        >>> result.val
        2
        >>> result.right.val
        3
        >>> result.left.val
        1
        """
        if self.is_leaf(tree) or self.is_balance(tree):
            return tree

        tree.left = self.rebalance(tree.left)
        tree.right = self.rebalance(tree.right)
        if self.is_balance(tree):
            return tree
        else:
            left_height = self.height(tree.left)
            right_height = self.height(tree.right)
            if right_height - left_height > 1:
                new_root = tree.right
                p = self.find_parent(tree.val, new_root)
                p.left = tree
                tree.right = None
                return self.rebalance(new_root)
            else:
                new_root = tree.left
                p = self.find_parent(tree.val, new_root)
                p.right = tree
                tree.left = None
                return self.rebalance(new_root)

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

        """
        if head is None:
            return None

        node = head
        tree = None
        while node:
            tree = self.cons(node.val, tree)
            tree = self.rebalance(tree)
            node = node.next

        return tree

