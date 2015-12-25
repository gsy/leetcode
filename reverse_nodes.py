__author__ = 'guang'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    @staticmethod
    def append(node, val):
        if node is None:
            return ListNode(val)
        else:
            new_node = ListNode(val)
            node.next = new_node
            return new_node

    @staticmethod
    def fromList(l):
        """
        >>> ls = LinkedList()
        >>> head = ls.fromList([1,2,3])
        >>> ls.toList(head)
        [1, 2, 3]
        """
        result = None
        tail = None
        first = True
        for x in l:
            tail = LinkedList.append(tail, x)
            if first:
                result = tail
                first = False

        return result

    @staticmethod
    def toList(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next

        return result

class Solution(object):
    def reverse(self, node, k):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5, 6])
        >>> result = s.reverse(head, 2)
        >>> head, tail, beyond_tail = result
        >>> head.val
        2
        >>> tail.val
        1
        >>> beyond_tail.val
        3
        >>> head = LinkedList.fromList([1])
        >>> result = s.reverse(head, 2)[0]
        >>> LinkedList.toList(result)
        [1]
        """
        if node is None:
            return None, None, None
        if k == 1:
            head = node
            tail = node
            beyond_tail = node.next
            return head, tail, beyond_tail
        else:
            head, tail, beyond_tail = self.reverse(node.next, k - 1)
            # touch the end, reverse
            if tail:
                tail.next = node
                return head, node, beyond_tail
            # k > len(node), do nothing
            else:
                return node, None, None

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([1])
        >>> result = s.reverseKGroup(head, 2)
        >>> LinkedList.toList(result)
        [1]
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5, 6])
        >>> result = s.reverseKGroup(head, 2)
        >>> LinkedList.toList(result)
        [2, 1, 4, 3, 6, 5]
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.reverseKGroup(head, 2)
        >>> LinkedList.toList(result)
        [2, 1, 4, 3, 5]
        >>> head = LinkedList.fromList([1, 2])
        >>> result = s.reverseKGroup(head, 3)
        >>> LinkedList.toList(result)
        [1, 2]
        """
        if head is None:
            return None

        rhead, rtail, beyond_tail = self.reverse(head, k)
        result = rhead
        while beyond_tail:
            new_head, new_tail, new_beyond_tail = self.reverse(beyond_tail, k)
            rtail.next = new_head
            rtail = new_tail
            beyond_tail = new_beyond_tail

        if rtail:
            rtail.next = None
        return result








