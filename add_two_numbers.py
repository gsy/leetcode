# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def calculate(self, values):
        total, acc = sum(values), 0
        if total >= 10:
            acc = int(total / 10)
            total = total % 10
        return total, acc

    def addTwoNumbers(self, l1, l2):
        acc, total = 0, 0
        head1, head2 = l1, l2
        root, prev, current = None, None, None

        while head1 and head2:
            total, acc = self.calculate([head1.val, head2.val, acc])
            head1 = head1.next
            head2 = head2.next
            current = ListNode(total)
            if root is None:
                root = current
            if prev is not None:
                prev.next = current
            prev = current

        while head1:
            total, acc = self.calculate([head1.val, acc])
            head1 = head1.next
            current = ListNode(total)
            if root is None:
                root = current
            if prev is not None:
                prev.next = current
            prev = current

        while head2:
            total, acc = self.calculate([head2.val, acc])
            head2 = head2.next
            current = ListNode(total)
            if root is None:
                root = current
            if prev is not None:
                prev.next = current
            prev = current

        if acc > 0:
            current = ListNode(acc)
            if root is None:
                root = current
            if prev is not None:
                prev.next = current
            prev = current

        return root

def printls(ls):
    while ls is not None:
        print(ls.val)
        ls = ls.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(6)
    r = s.addTwoNumbers(l1, l2)
    printls(r)
