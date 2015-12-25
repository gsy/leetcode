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
        >>> LinkedList.toList(result)
        [2, 1, 3, 4, 5, 6]
        """
        if node is None:
            return None, None
        if k == 1:
            tail = node
            beyond_tail = node.next
            return tail, beyond_tail
        else:
            tail, beyond_tail = self.reverse(node.next, k - 1)
            # touch the end, reverse
            if tail:
                tail.next = node
            # k > len(node), do nothing
            else:
                pass



    def kth(self, head, k):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> one = s.kth(head, 1)
        >>> one.val
        1
        >>> two = s.kth(head, 2)
        >>> two.val
        2
        >>> s.kth(head, 5)

        >>> three = s.kth(head, 3)
        >>> three.val
        3
        """
        while True:
            if head is None:
                return None
            if k == 1:
                return head
            head = head.next
            k -= 1

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5, 6])
        >>> result = s.reverseKGroup(head, 3)
        >>> LinkedList.toList(result)
        [3, 2, 1, 4, 5, 6]
        >>> head = LinkedList.fromList([1])
        >>> result = s.reverseKGroup(head, 2)
        >>> LinkedList.toList(result)
        [1]
        """
        if head is None:
            return None

        # length = len(head)
        self.reverse(head, k)



