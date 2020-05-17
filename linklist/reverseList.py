# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        prev = None
        node = head

        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev
