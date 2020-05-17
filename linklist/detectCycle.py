#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        hasCycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                hasCycle = True
                break

        if not hasCycle:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

if __name__ == '__main__':
    s = Solution()
    head = ListNode(3)
    a = ListNode(2)
    head.next = a
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = a
    r = s.detectCycle(head)
    print(r, r.val)
