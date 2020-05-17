#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1 = headA
        n2 = headB

        len1, last1 = 0, None
        while n1:
            len1 += 1
            last1 = n1
            n1 = n1.next

        len2, last2 = 0, None
        while n2:
            len2 += 1
            last2 = n2
            n2 = n2.next

        if last1 != last2:
            return None

        node1, node2 = headA, headB
        if len1 > len2:
            len1, len2 = len2, len1
            node1, node2 = headB, headA

        for i in range(len2-len1):
            node2 = node2.next

        for i in range(len1):
            if node1 == node2:
                return node1
            else:
                node1 = node1.next
                node2 = node2.next

        return None
