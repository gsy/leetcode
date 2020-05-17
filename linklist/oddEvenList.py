#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        oddHead = head
        evenHead = head.next

        oddNode = oddHead
        evenNode = evenHead

        done = False
        while not done:
            oddNext = None
            if oddNode.next and oddNode.next.next:
                oddNext = oddNode.next.next
            else:
                done = True

            evenNext = None
            if evenNode.next and evenNode.next.next:
                evenNext = evenNode.next.next
            else:
                done = True

            oddNode.next = oddNext
            evenNode.next = evenNext

            if oddNext is not None:
                oddNode = oddNext
            if evenNext is not None:
                evenNode = evenNext

        oddNode.next = evenHead
        return oddHead
