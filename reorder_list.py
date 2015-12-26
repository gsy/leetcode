__author__ = 'guang'

from linklist import LinkedList, ListNode

class Solution(object):
    def length(self, head):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> s.length(head)
        3
        >>> s.length(None)
        0
        """
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        return count

    def kth(self, head, k):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.kth(head, 1)
        >>> result.val
        1
        >>> result = s.kth(head, 3)
        >>> result.val
        3
        >>> result = s.kth(head, 5)
        >>> result.val
        5
        >>> result = s.kth(head, 10)
        >>> result is None
        True
        """
        if head is None:
            return None

        count = 1
        node = head
        while node and count < k:
            count += 1
            node = node.next

        return node

    def empty(self, ls):
        if ls is None:
            return True

        head, tail = ls
        return head is None and tail is None

    def cons(self, a, ls):
        """
        >>> s = Solution()
        >>> a = ListNode(3)
        >>> ls = None, None
        >>> result = s.cons(a, ls)
        >>> head, tail = result
        >>> head.val
        3
        >>> tail.val
        3
        """
        if a is None:
            return ls
        elif self.empty(ls):
            a.next = None
            return a, a
        else:
            head, tail = ls
            a.next = head
            return a, tail

    def append(self, a, ls):
        if a is None:
            return ls
        elif self.empty(ls):
            a.next = None
            return a, a
        else:
            head, tail = ls
            tail.next = a
            a.next = None
            return head, a

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

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1, 5, 2, 4, 3]
        >>> head = LinkedList.fromList([1, 2, 3, 4])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1, 4, 2, 3]
        >>> head = LinkedList.fromList([])
        >>> s.reorderList(head)

        >>> head = LinkedList.fromList([1])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1]
        >>> head = LinkedList.fromList([1, 2])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1, 2]
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> s.reorderList(head)
        >>> LinkedList.toList(head)
        [1, 3, 2]
        """

        if head is None:
            return None

        length = self.length(head)
        if length <= 2:
            return

        if length % 2 == 0:
            left_index = length / 2
            right_index = length / 2 + 1
        else:
            left_index = length / 2 + 1
            right_index = left_index

        count = 1
        stack = []
        tail = None, None
        node = head
        while node:
            if count < left_index:
                stack.append(node)
                node = node.next
            elif count == left_index or count == right_index:
                succeeding = node.next
                tail = self.append(node, tail)
                node = succeeding
            elif count > right_index:
                left = stack.pop()
                succeeding = node.next
                right = self.cons(node, None)
                pair = self.cons(left, right)
                tail = self.concat(pair, tail)
                node = succeeding
            count += 1

