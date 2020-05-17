class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None or head.next is None:
            return head

        leftHead, rightHead = None, None
        leftPrev, rightPrev = None, None

        node = head
        while node:
            if node.val < x:
                leftNode = node

                if leftHead is None:
                    leftHead = leftNode
                if leftPrev:
                    leftPrev.next = leftNode
                leftPrev = leftNode
            else:
                rightNode = node

                if rightHead is None:
                    rightHead = rightNode
                if rightPrev:
                    rightPrev.next = rightNode
                rightPrev = rightNode
            node = node.next

        if rightPrev:
            rightPrev.next = None

        if leftHead:
            leftPrev.next = rightHead
            return leftHead

        else:
            return rightHead
