#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head, G):
        if head is None:
            return 0

        node = head
        newComponent = False
        result = 0

        while node:
            if node.val in G:
                if not newComponent:
                    newComponent = True
                    result = result + 1
            else:
                newComponent = False

            node = node.next
        return result
