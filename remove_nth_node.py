__author__ = 'guang'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def length(self, head):
        if head is None:
            return 0
        else:
            return 1 + self.length(head.next)

    def nth(self, head, n):
        i = 1
        while head is not None:
            if i == n:
                return head
            else:
                i += 1
                head = head.next

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        >>> s = Solution()
        >>> s.removeNthFromEnd([1], 1)
        """
        # length
        total = self.length(head)
        # reverse
        m = total - n
        if m == 0:
            head = head.next
        else:
            x = self.nth(head, m)
            # remove
            y = x.next
            x.next = y.next

        return head





