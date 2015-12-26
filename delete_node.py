__author__ = 'guang'


from linklist import LinkedList, ListNode

class Solution(object):
    def isTail(self, node):
        return node is not None and node.next is None

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        >>> s = Solution()
        >>> one = ListNode(1)
        >>> two = ListNode(2)
        >>> three = ListNode(3)
        >>> four = ListNode(4)
        >>> one.next, two.next, three.next = two, three, four
        >>> s.deleteNode(two)
        >>> LinkedList.toList(one)
        [1, 3, 4]
        """
        if node is None:
            return

        while node:
            succeeding = node.next
            if self.isTail(succeeding):
                node.val = succeeding.val
                node.next = None
                break
            else:
                node.val = succeeding.val
                node = node.next

