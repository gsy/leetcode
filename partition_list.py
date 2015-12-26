__author__ = 'guang'

from linklist import LinkedList, ListNode

class Solution(object):
    def empty(self, ls):
        head, tail = ls
        return head is None and tail is None

    def append(self, node, ls):
        """
        >>> s = Solution()
        >>> node = ListNode(3)
        >>> head = LinkedList.fromList([1, 2, 4])
        >>> tail = head.next.next
        >>> result = s.append(node, (head, tail))
        >>> LinkedList.toList(result[0])
        [1, 2, 4, 3]
        >>> head = LinkedList.fromList([1, 2, 4])
        >>> result = s.append(None, (head, tail))
        >>> LinkedList.toList(result[0])
        [1, 2, 4]
        """
        if node is None:
            return ls

        head, tail = ls
        if self.empty(ls):
            head = node
            tail = node
            tail.next = None
        else:
            tail.next = node
            tail = node
            tail.next = None

        return head, tail

    def concat(self, ls1, ls2):
        if self.empty(ls1):
            return ls2
        elif self.empty(ls2):
            return ls1
        else:
            head1, tail1 = ls1
            head2, tail2 = ls2

            tail1.next = head2
            return head1, tail2

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([1,4,3,2,5,2])
        >>> result = s.partition(head, 3)
        >>> LinkedList.toList(result)
        [1, 2, 2, 4, 3, 5]
        >>> head = LinkedList.fromList([1,4,3,2,5,2])
        >>> result = s.partition(head, 10)
        >>> LinkedList.toList(result)
        [1, 4, 3, 2, 5, 2]
        >>> head = LinkedList.fromList([1,4,3,2,5,2])
        >>> result = s.partition(head, 0)
        >>> LinkedList.toList(result)
        [1, 4, 3, 2, 5, 2]
        >>> head = LinkedList.fromList([1, 1, 1, 1, 1])
        >>> result = s.partition(head, 1)
        >>> LinkedList.toList(result)
        [1, 1, 1, 1, 1]
        """

        if head is None:
            return None

        smaller, greater = (None, None), (None, None)

        node = head
        while node:
            succeeding = node.next
            if node.val < x:
                smaller = self.append(node, smaller)
            else:
                greater = self.append(node, greater)
            node = succeeding

        result = self.concat(smaller, greater)
        return result[0]

