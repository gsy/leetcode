#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> int:
        if head is None:
            return None

        length = 0
        node = head
        while node:
            length = length + 1
            node = node.next

        if k > length:
            return None
       
        node = head
        for i in range(length - k):
            node = node.next

        return node
