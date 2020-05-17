#!/usr/bin/env python3


class Solution:
    def nextLargerNodes(self, head):
        if head is None:
            return []

        node = head
        stack = []
        result = []
        index = 0
        while node:
            if len(stack) > 0:
                print("stack", stack)
                while len(stack) > 0:
                    i, last = stack[-1]
                    if node.val > last:
                        stack.pop(-1)
                        result[i] = node.val
                    else:
                        break
            stack.append((index, node.val))
            result.append(0)
            index = index + 1
            node = node.next
        return result

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    s = Solution()
    a = ListNode(2)
    a.next = ListNode(1)
    a.next.next = ListNode(5)
    ls = s.nextLargerNodes(a)
    print(ls)

    b = ListNode(1)
    b.next = ListNode(7)
    b.next.next = ListNode(5)
    b.next.next.next = ListNode(1)
    b.next.next.next.next = ListNode(9)
    b.next.next.next.next.next = ListNode(2)
    b.next.next.next.next.next.next = ListNode(5)
    b.next.next.next.next.next.next.next = ListNode(1)
    ls = s.nextLargerNodes(b)
    print(ls)
