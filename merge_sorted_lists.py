__author__ = 'guang'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, node, val):
        if node is None:
            return ListNode(val)
        else:
            new_node = ListNode(val)
            node.next = new_node
            return new_node

    def fromList(self, l):
        """
        >>> s = ListNode(None)
        >>> head = s.fromList([1,2,3])
        >>> s.toList(head)
        [1, 2, 3]
        """
        result = None
        tail = None
        first = True
        for x in l:
            tail = self.append(tail, x)
            if first:
                result = tail
                first = False

        return result

    def toList(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next

        return result


class Solution(object):
    def append(self, node, val):
        if node is None:
            return ListNode(val)
        else:
            new_node = ListNode(val)
            node.next = new_node
            return new_node

    def merge2Lists(self, a, b):
        """
        >>> s = Solution()
        >>> a = ListNode(None).fromList([2, 3, 4])
        >>> b = ListNode(None).fromList([1, 2, 5])
        >>> result = s.merge2Lists(a, b)
        >>> ListNode(None).toList(result)
        [1, 2, 2, 3, 4, 5]
        >>> a = None
        >>> b = ListNode(None).fromList([1, 2, 5])
        >>> result = s.merge2Lists(a, b)
        >>> ListNode(None).toList(result)
        [1, 2, 5]
        """

        if a is None and b is None:
            return None
        elif a is None:
            return b
        elif b is None:
            return a
        else:
            first = True
            result = None
            tail = None
            nodea = a
            nodeb = b
            while nodea and nodeb:
                x = nodea.val
                y = nodeb.val
                if x <= y:
                    value = x
                    nodea = nodea.next
                else:
                    value = y
                    nodeb = nodeb.next
                tail = self.append(tail, value)
                if first:
                    result = tail
                    first = False

            while nodea:
                tail = self.append(tail, nodea.val)
                nodea = nodea.next

            while nodeb:
                tail = self.append(tail, nodeb.val)
                nodeb = nodeb.next

            return result

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        >>> s = Solution()
        >>> a = ListNode(None).fromList([1, 2, 3])
        >>> b = ListNode(None).fromList([3, 4, 5])
        >>> c = ListNode(None).fromList([8, 9, 13])
        >>> lists = [a, b, c]
        >>> result = s.mergeKLists(lists)
        >>> ListNode(None).toList(result)
        [1, 2, 3, 3, 4, 5, 8, 9, 13]
        """
        length = len(lists)
        if length == 0:
            return None

        if length == 1:
            return lists[0]

        elif length == 2:
            a = lists[0]
            b = lists[1]
            return self.merge2Lists(a, b)

        else:
            middle = length / 2
            a = self.mergeKLists(lists[:middle+1])
            b = self.mergeKLists(lists[middle+1:])
            return self.merge2Lists(a, b)
