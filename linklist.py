__author__ = 'guang'

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
