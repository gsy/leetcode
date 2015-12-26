__author__ = 'guang'

from linklist import LinkedList

class Solution(object):
    def length(self, head):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> s.length(head)
        3
        >>> s.length(None)
        0
        """
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        return count

    def kth(self, head, k):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.kth(head, 1)
        >>> result.val
        1
        >>> result = s.kth(head, 3)
        >>> result.val
        3
        >>> result = s.kth(head, 5)
        >>> result.val
        5
        >>> result = s.kth(head, 10)
        >>> result is None
        True
        """
        if head is None:
            return None

        count = 1
        node = head
        while node and count < k:
            count += 1
            node = node.next

        return node

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1, 5, 2, 4, 3]
        >>> head = LinkedList.fromList([1, 2, 3, 4])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1, 4, 2, 3]
        >>> head = LinkedList.fromList([])
        >>> s.reorderList(head)

        >>> head = LinkedList.fromList([1])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1]
        >>> head = LinkedList.fromList([1, 2])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1, 2]
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1, 3, 2]
        """

        if head is None:
            return None

        length = self.length(head)
        if length <= 2:
            return

        node = head
        succeeding = node.next
        precede_tail = self.kth(head, length - 1)
        tail = precede_tail.next

        node.next = tail
        tail.next = succeeding
        precede_tail.next = None

        self.reorderList(succeeding)

