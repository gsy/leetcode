#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length <= 1:
            return True

        mid = length // 2

        prev = None
        current = head

        for i in range(mid):
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        if length % 2 == 0:
            a, b = prev, current
        else:
            a, b = prev, current.next


        while a and b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next

        return True
