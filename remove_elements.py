__author__ = 'guang'

from linklist import LinkedList

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 6, 3, 4, 5, 6])
        >>> result = s.removeElements(head, 6)
        >>> LinkedList.toList(result)
        [1, 2, 3, 4, 5]
        >>> s.removeElements(None, 3)

        >>> head = LinkedList.fromList([1, 1, 1, 1, 1])
        >>> result = s.removeElements(head, 1)
        >>> result

        >>> head = LinkedList.fromList([6, 1, 2, 6, 3, 4, 5, 6])
        >>> result = s.removeElements(head, 6)
        >>> LinkedList.toList(result)
        [1, 2, 3, 4, 5]
        >>> head = LinkedList.fromList([1, 2, 2, 1])
        >>> result = s.removeElements(head, 2)
        >>> LinkedList.toList(result)
        [1, 1]
        """
        if head is None:
            return None

        while head:
            if head.val == val:
                head = head.next
            else:
                break

        node = head
        while node:
            next_node = node.next
            while next_node:
                if next_node.val == val:
                    node.next = next_node.next
                    next_node = next_node.next
                else:
                    break
            node = next_node

        return head
