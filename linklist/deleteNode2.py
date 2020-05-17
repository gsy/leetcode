#!/usr/bin/env python3

class Solution:
    def deleteNode2(self, head, val):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        if node is None:
            return None

        sentinal = ListNode(0)
        sentinal.next = head

        prev = sentinal
        node = sentinal.next

        while node:
            if node.val == val:
                prev.next = node.next
                node = None
                break
            else:
                prev = node
                node = node.next

        return sentinal.next
