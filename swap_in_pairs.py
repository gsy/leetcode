__author__ = 'guang'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swap(self, node):
        """
        >>> s = Solution()
        >>> one = ListNode(1)
        >>> two = ListNode(2)
        >>> three = ListNode(3)
        >>> four = ListNode(4)
        >>> one.next, two.next, three.next = two, three, four
        >>> s.swap(one)
        >>> one.next.val
        3
        >>> two.next.val
        1
        """
        if node is None:
            return None

        a = node
        b = node.next
        if b is None:
            return a
        else:
            c = b.next
            b.next = a
            a.next = c
        return b

    def toList(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next

        return result

    def fromList(self, ls):
        if not ls:
            return None
        head = ListNode(ls[0])
        current = head
        for i in range(1, len(ls)):
            node = ListNode(ls[i])
            current.next = node
            current = node

        return head

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> one = ListNode(1)
        >>> two = ListNode(2)
        >>> three = ListNode(3)
        >>> four = ListNode(4)
        >>> one.next, two.next = two, three
        >>> result = s.swapPairs(one)
        >>> s.toList(result)
        [2, 1, 3]
        >>> single = ListNode(1)
        >>> result = s.swapPairs(single)
        >>> s.toList(result)
        [1]
        >>> head = s.fromList([1, 2])
        >>> s.toList(head)
        [1, 2]
        >>> head = s.swapPairs(head)
        >>> s.toList(head)
        [2, 1]
        """
        if head is None:
            return None

        head = self.swap(head)
        current = head.next
        while current:
            new_head = self.swap(current.next)
            current.next = new_head
            if new_head:
                current = new_head.next
            else:
                break

        return head










