#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i, j = head, head

        while j:
            j = j.next
            if j:
                j = j.next
            else:
                break
            i = i.next
        return i
