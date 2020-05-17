class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers2(self, l1, l2):
        stack1 = []
        stack2 = []

        a = l1
        b = l2
        while a:
            stack1.append(a.val)
            a = a.next
        while b:
            stack2.append(b.val)
            b = b.next

        head = ListNode(0)
        carry = 0
        while len(stack1) > 0 or len(stack2) > 0:
            if len(stack1) > 0 and len(stack2) > 0:
                total = stack1.pop(-1) + stack2.pop(-1) + carry
            elif len(stack1) > 0:
                total = stack1.pop(-1) + carry
            else:
                total = stack2.pop(-1) + carry
            digit = total % 10
            carry = total // 10

            node = ListNode(digit)
            node.next = head.next
            head.next = node

        if carry > 0:
            node = ListNode(carry)
            node.next = head.next
            head.next = node

        return head.next
