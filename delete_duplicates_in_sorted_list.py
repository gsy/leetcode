__author__ = 'guang'

from linklist import LinkedList, ListNode

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> result = s.deleteDuplicates(head)
        >>> LinkedList.toList(result)
        [1, 2, 3]
        >>> head = LinkedList.fromList([1, 1, 1])
        >>> result = s.deleteDuplicates(head)
        >>> result

        >>> head = LinkedList.fromList([1, 2, 3, 3, 4, 4, 5])
        >>> result = s.deleteDuplicates(head)
        >>> LinkedList.toList(result)
        [1, 2, 5]
        >>> head = LinkedList.fromList([1, 1, 1, 2, 3])
        >>> result = s.deleteDuplicates(head)
        >>> LinkedList.toList(result)
        [2, 3]
        """

        if head is None:
            return None

        value = head.val
        succeeding = head.next
        if succeeding and succeeding.val == value:
            while head and head.val == value:
                head = head.next

            if head is None:
                return None
            else:
                return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head

