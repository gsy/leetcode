# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def splitListToParts(self, root, k):
        length = 0
        node = root
        while node:
            length = length + 1
            node = node.next

        lens = []
        average = length // k
        extra = length % k

        for i in range(k):
            if extra > 0:
                take = average + 1
                extra -= 1
            else:
                take = average
            lens.append(take)

        result = []
        node = root
        for l in lens:
            count = 0
            head = node
            while node:
                count = count + 1
                tmp = node.next

                if count == l:
                    node.next = None
                    node = tmp
                    break
                else:
                    node = node.next
            result.append(head)
        return result
