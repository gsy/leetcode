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

    def helper(self, node, start, end):
        """
        >>> s = Solution()
        >>> node = LinkedList.fromList([4, 5])
        >>> tree, head = s.helper(node, 4, 5)
        >>> tree.val
        5
        >>> tree.left.val
        4
        >>> head.val
        5
        >>> node = LinkedList.fromList([1, 2])
        >>> tree, head = s.helper(node, 1, 2)
        >>> tree.val
        2
        >>> tree.left.val
        1
        >>> head.val
        2
        >>> node = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> tree, head = s.helper(node, 1, 5)
        >>> head.val
        5

        # >>> BST(tree).show()

        >>> node = LinkedList.fromList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        >>> tree, head = s.helper(node, 1, 15)
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
        left, head = self.helper(node, start, middle - 1)
        head = head.next
        root = TreeNode(head.val)
        root.left = left
        head = head.next
        right, new_head = self.helper(head, middle + 1, end)
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
        return self.helper(head, 1, length)[0]



