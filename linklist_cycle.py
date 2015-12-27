__author__ = 'guang'

from linklist import LinkedList, ListNode

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        >>> s = Solution()
        >>> one, two, three, four, five = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
        >>> one.next, two.next, three.next, four.next = two, three, four, five
        >>> LinkedList.toList(one)
        [1, 2, 3, 4, 5]
        >>> s.hasCycle(one)
        False
        >>> one.next, two.next, three.next, four.next = two, three, four, five
        >>> five.next = two
        >>> s.hasCycle(one)
        True
        >>> one.next, two.next, three.next, four.next = two, three, four, five
        >>> one.next = two
        >>> two.next = one
        >>> s.hasCycle(one)
        True
        """
        if head is None:
            return False

        elif head.next is None:
            return False

        first, second = head, head.next
        go_ahead, steps = 1, 1

        while first and second:
            if second == first:
                return True

            elif go_ahead < steps:
                go_ahead += 1
                second = second.next
            else:
                steps *= 2
                go_ahead = 1
                first = second
                second = first.next

        return False









