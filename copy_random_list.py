__author__ = 'guang'


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def to_list(self):
        result = [self.label]
        node = self.next
        while node:
            result.append(node.label)
            node = node.next
        return result

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        >>> s = Solution()
        >>> one, two, three, four = RandomListNode(1), RandomListNode(2), RandomListNode(3), RandomListNode(4)
        >>> one.next, two.next, three.next = two, three, four
        >>> one.random, three.random = four, one
        >>> one.to_list()
        [1, 2, 3, 4]
        >>> copy = s.copyRandomList(one)
        >>> copy.to_list()
        [1, 2, 3, 4]
        >>> copy.random.label
        4
        >>> copy.next.next.random.label
        1
        """
        if head is None:
            return None

        copy_head = None
        copy_tail = None
        origin_copy_mapping = {}

        node = head
        # copy value
        while node:
            copy = RandomListNode(node.label)
            if copy_tail is None:
                copy_head = copy
                copy_tail = copy
            else:
                copy_tail.next = copy
                copy_tail = copy
            origin_copy_mapping[node] = copy
            node = node.next

        # copy random pointer
        node = head
        while node:
            if node.random:
                random = node.random
                copy = origin_copy_mapping[node]
                random_copy = origin_copy_mapping[random]
                copy.random = random_copy
            node = node.next

        return copy_head


