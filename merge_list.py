__author__ = 'guang'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def append(self, node, x):
        """
        >>> s = Solution()
        >>> head = ListNode(10)
        >>> x = s.append(head, 10) # doctest:+ELLIPSIS
        >>> head.next.val == 10
        True
        """
        new_node = ListNode(x)
        if node is not None:
            node.next = new_node

        return new_node

    def toList(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> l1 = ListNode(1)
        >>> x = s.append(l1, 3)
        >>> y = s.append(x, 5)
        >>> l2 = ListNode(2)
        >>> i = s.append(l2, 4)
        >>> j = s.append(i, 6)
        >>> merged = s.mergeTwoLists(l1, l2)
        >>> s.toList(merged)
        [1, 2, 3, 4, 5, 6]
        >>> s.mergeTwoLists(None, None)

        >>> result = s.mergeTwoLists(None, l2)
        >>> result != l2
        True
        >>> s.toList(result)
        [2, 4, 6]
        """

        if l1 is None and l2 is None:
            return None

        pointer1 = l1
        pointer2 = l2
        result = None
        node = None

        while not (pointer1 is None and pointer2 is None):
            if pointer1 is None:
                value = pointer2.val
                pointer2 = pointer2.next
            elif pointer2 is None:
                value = pointer1.val
                pointer1 = pointer1.next
            else:
                x = pointer1.val
                y = pointer2.val
                if x >= y:
                    value = y
                    pointer2 = pointer2.next
                else:
                    value = x
                    pointer1 = pointer1.next

            node = self.append(node, value)

            if result is None:
                result = node

        return result


