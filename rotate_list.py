__author__ = 'guang'

from linklist import ListNode, LinkedList


class Solution(object):
    def tail(self, head):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> result = s.tail(head)
        >>> result.val
        3
        >>> head = LinkedList.fromList([])
        >>> result = s.tail(head)
        >>> result

        >>> head = LinkedList.fromList([1])
        >>> result = s.tail(head)
        >>> result.val
        1
        """
        node = head
        while node:
            if node.next is None:
                break
            node = node.next

        return node

    def length(self, head):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> s.length(head)
        3
        >>> head = LinkedList.fromList([])
        >>> s.length(head)
        0
        >>> head = LinkedList.fromList([1])
        >>> s.length(head)
        1
        """
        result = 0
        node = head
        while node:
            result += 1
            if node.next is None:
                break
            node = node.next

        return result

    def kth(self, head, k):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([])
        >>> result = s.kth(head, 10)
        >>> result

        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.kth(head, 5)
        >>> result.val
        5
        """
        if head is None:
            return None

        count = 1
        node = head
        while count < k:
            node = node.next
            count += 1
        return node

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.rotateRight(head, 2)
        >>> LinkedList.toList(result)
        [4, 5, 1, 2, 3]
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.rotateRight(head, 3)
        >>> LinkedList.toList(result)
        [3, 4, 5, 1, 2]
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.rotateRight(head, 10)
        >>> LinkedList.toList(result)
        [1, 2, 3, 4, 5]
        """
        if head is None:
            return None

        if k == 0:
            return head

        length = self.length(head)
        tail = self.tail(head)

        tail.next = head
        remain = length - (k % length)
        new_tail = self.kth(head, remain)
        new_head = new_tail.next
        new_tail.next = None

        return new_head
