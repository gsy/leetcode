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
    def append(self, a, b):
        if a is None:
            return b
        else:
            a.next = b
            return b

    def divide(self, head, x):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([3, 5, 7, 7, 8, 8, 3])
        >>> smaller, greater = s.divide(head, 7)
        >>> LinkedList.toList(greater)
        [7, 7, 8, 8]
        >>> LinkedList.toList(smaller)
        [3, 5, 3]
        >>> head = LinkedList.fromList([10, 2, 3, 4, 5])
        >>> smaller, greater = s.divide(head, 20)
        >>> LinkedList.toList(greater)
        []
        >>> LinkedList.toList(smaller)
        [10, 2, 3, 4, 5]

        """
        if head is None:
            return None, None, None, None

        node, smaller, equal, greater = head, None, None, None
        tail1, tail2, tail3 = None, None, None
        while node:
            value = node.val
            next = node.next
            if value < x:
                tail1 = self.append(tail1, node)
                tail1.next = None
                if smaller is None:
                    smaller = tail1
            elif value == x:
                tail2 = self.append(tail2, node)
                tail2.next = None
                if equal is None:
                    equal = tail2
            else:
                tail3 = self.append(tail3, node)
                tail3.next = None
                if greater is None:
                    greater = tail3

            node = next

        return smaller, equal, tail2, greater

    def sizeEqualTwo(self, head):
        return head is not None and head.next is not None and head.next.next is None

    def empty(self, link_list):
        head, tail = link_list
        return head is None and tail is None

    def cons(self, node, link_list):
        if node is None:
            return link_list
        elif self.empty(link_list):
            node.next = None
            return node, node
        else:
            head, tail = link_list
            node.next = head
            return node, tail

    def concat(self, link_list1, link_list2):
        if self.empty(link_list1):
            return link_list2
        elif self.empty(link_list2):
            return link_list1
        else:
            head1, tail1 = link_list1
            head2, tail2 = link_list2
            head = head1
            tail1.next = head2
            tail = tail2
            return head, tail

    def sort(self, head):
        if head is None:
            return None, None
        elif head.next is None:
            return head, head
        elif self.sizeEqualTwo(head):
            a, b = head, head.next
            if a.val > b.val:
                b.next = a
                a.next = None
                return b, a
            else:
                return a, b
        else:
            pilot = head
            smaller, equal, equal_tail, greater = self.divide(head.next, pilot.val)
            head1, tail1 = self.sort(smaller)
            head2, tail2 = self.cons(pilot, (equal, equal_tail))
            head3, tail3 = self.sort(greater)

            new_head, new_tail = self.concat((head1, tail1), (head2, tail2))
            new_head, new_tail = self.concat((new_head, new_tail), (head3, tail3))

            return new_head, new_tail

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([2, 1, 4, 3])
        >>> result = s.sortList(head)
        >>> LinkedList.toList(result)
        [1, 2, 3, 4]
        >>> head = LinkedList.fromList([])
        >>> result = s.sortList(head)

        >>> head = LinkedList.fromList([1])
        >>> result = s.sortList(head)
        >>> LinkedList.toList(result)
        [1]
        >>> head = LinkedList.fromList([3, 2, 1])
        >>> result = s.sortList(head)
        >>> LinkedList.toList(result)
        [1, 2, 3]
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> result = s.sortList(head)
        >>> LinkedList.toList(result)
        [1, 2, 3]
        >>> head = LinkedList.fromList([1, 1, 1, 1])
        >>> result = s.sortList(head)
        >>> LinkedList.toList(result)
        [1, 1, 1, 1]
        >>> head = LinkedList.fromList([1, 3, 7, 7, 8, 8, 5])
        >>> result = s.sortList(head)
        >>> LinkedList.toList(head)
        [1, 3, 5, 7, 7, 8, 8]
        """
        return self.sort(head)[0]









