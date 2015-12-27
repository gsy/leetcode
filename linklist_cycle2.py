__author__ = 'guang'

from linklist import LinkedList, ListNode

class Solution(object):
    def find_cycle_begin(self, head, length):
        node = head
        while node:
            succeeding = node.next
            for i in range(length - 1):
                succeeding = succeeding.next
            if node == succeeding:
                return node
            else:
                node = node.next

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        >>> s = Solution()
        >>> one, two, three, four, five = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
        >>> one.next, two.next, three.next, four.next = two, three, four, five
        >>> LinkedList.toList(one)
        [1, 2, 3, 4, 5]
        >>> s.detectCycle(one)

        >>> one.next, two.next, three.next, four.next = two, three, four, five
        >>> five.next = two
        >>> result = s.detectCycle(one)
        >>> result.val
        2
        >>> one.next, two.next, three.next, four.next = two, three, four, five
        >>> two.next = one
        >>> result = s.detectCycle(one)
        >>> result.val
        1
        """
        if head is None:
            return None

        elif head.next is None:
            return None

        first, second = head, head.next
        go_ahead, steps = 1, 1
        cycle_length = 0

        while first and second:
            if second == first:
                cycle_length = go_ahead
                break

            elif go_ahead < steps:
                go_ahead += 1
                second = second.next
            else:
                steps *= 2
                go_ahead = 1
                first = second
                second = first.next

        if cycle_length == 0:
            return None

        else:
            return self.find_cycle_begin(head, cycle_length)

