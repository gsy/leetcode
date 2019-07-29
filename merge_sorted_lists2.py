# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head1 = l1
        head2 = l2
        root, prev = None, None

        while head1 and head2:
            value = None
            if head1.val <= head2.val:
                value = head1.val
                head1 = head1.next
            else:
                value = head2.val
                head2 = head2.next

            current = ListNode(value)
            if root is None:
                root = current
            if prev is not None:
                prev.next = current
            prev = current

        while head1:
            current = ListNode(head1.val)
            head1 = head1.next
            if root is None:
                root = current
            if prev is not None:
                prev.next = current
            prev = current

        while head2:
            current = ListNode(head2.val)
            head2 = head2.next
            if root is None:
                root = current
            if prev is not None:
                prev.next = current
            prev = current

        return root


def printls(ls):
    while ls:
        print(ls.val,)
        ls = ls.next


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    r = s.mergeTwoLists(l1, l2)
    printls(r)

    print('-'*20)
    l1 = None
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    r = s.mergeTwoLists(l1, l2)
    printls(r)
