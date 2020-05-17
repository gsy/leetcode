
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        if head is None:
            return None

        ls = []
        length = 0
        node = head

        while node:
            ls.append(node.val)
            length = length + 1
            node = node.next

        return ls[length - k]
