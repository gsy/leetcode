__author__ = 'guang'

from linklist import LinkedList

class Solution(object):
    def reverse(self, ls, m, n, k):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.reverse(head, 2, 4, 1)
        >>> LinkedList.toList(result[0])
        [1, 4, 3, 2, 5]
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.reverse(head, 1, 5, 1)
        >>> LinkedList.toList(result[0])
        [5, 4, 3, 2, 1]
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.reverse(head, 1, 1, 1)
        >>> LinkedList.toList(result[0])
        [1, 2, 3, 4, 5]
        """
        if ls is None:
            return None, None

        current = ls
        head, tail = self.reverse(current.next, m, n, k + 1)
        if m <= k <= n - 1 and tail:
            beyond_tail = tail.next
            tail.next = current
            current.next = beyond_tail
            return head, current
        else:
            current.next = head
            return current, current

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.reverseBetween(head, 2, 4)
        >>> LinkedList.toList(result)
        [1, 4, 3, 2, 5]
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.reverseBetween(head, 1, 5)
        >>> LinkedList.toList(result)
        [5, 4, 3, 2, 1]
        >>> s.reverseBetween(None, 1, 3)

        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.reverseBetween(head, 1, 2)
        >>> LinkedList.toList(result)
        [2, 1, 3, 4, 5]
        """
        return self.reverse(head, m, n, 1)[0]
