__author__ = 'guang'

from linklist import LinkedList

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 1, 2])
        >>> result = s.deleteDuplicates(head)
        >>> LinkedList.toList(result)
        [1, 2]
        >>> head = LinkedList.fromList([1, 1, 2, 3, 3])
        >>> result = s.deleteDuplicates(head)
        >>> LinkedList.toList(result)
        [1, 2, 3]
        """
        if head is None:
            return None

        current = head
        node = current.next
        already_scan = [current.val]
        while node:
            if node.val in already_scan:
                current.next = node.next
            else:
                already_scan.append(node.val)
                current = node
            node = node.next


        return head

