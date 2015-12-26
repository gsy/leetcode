__author__ = 'guang'

from linklist import LinkedList

class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([])
        >>> s.reverseList(head)

        >>> head = LinkedList.fromList([1, 2, 3])
        >>> result = s.reverseList(head)
        >>> LinkedList.toList(result)
        [3, 2, 1]
        """

        if head is None:
            return None

        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        tail = stack.pop()
        current = tail
        while stack:
            node = stack.pop()
            current.next = node
            current = node

        current.next = None

        return tail






