#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        seen = set()

        sentinel = ListNode(0)
        sentinel.next = head

        prev = sentinel
        node = prev.next

        while node:
            if node.val in seen:
                prev.next = node.next
                node = prev.next
                continue
            else:
                seen.add(node.val)

            prev = prev.next
            node = prev.next

        return sentinel.next
