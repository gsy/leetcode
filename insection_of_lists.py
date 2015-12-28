__author__ = 'guang'

from linklist import LinkedList, ListNode

class Solution(object):

    def length(self, head):
        """
        >>> s = Solution()
        >>> s.length(None)
        0
        >>> head = LinkedList.fromList([1])
        >>> s.length(head)
        1
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> s.length(head)
        3
        """
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> tail = LinkedList.fromList([4, 5, 6])
        >>> headA = LinkedList.fromList([1, 2])
        >>> headB = LinkedList.fromList([7, 8, 9])
        >>> headA.next.next = tail
        >>> headB.next.next.next = tail
        >>> LinkedList.toList(headA)
        [1, 2, 4, 5, 6]
        >>> LinkedList.toList(headB)
        [7, 8, 9, 4, 5, 6]
        >>> node = s.getIntersectionNode(headA, headB)
        >>> node.val
        4
        """
        if headA is None or headB is None:
            return None

        length1 = self.length(headA)
        length2 = self.length(headB)
        if length1 > length2:
            steps = length1 - length2
            slower = headB
            faster = headA
        else:
            steps = length2 - length1
            slower = headA
            faster = headB

        go_ahead = 0
        while slower and faster:
            if slower == faster:
                return slower
            elif go_ahead < steps:
                go_ahead += 1
                faster = faster.next
            else:
                slower = slower.next
                faster = faster.next

        return None
