__author__ = 'guang'

from linklist import ListNode, LinkedList

class Solution(object):

    def insertion_point(self, head, tail, target):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([7, 8])
        >>> tail, target = head, head.next
        >>> point = s.insertion_point(head, tail, target)
        >>> point.val
        7
        >>> head = LinkedList.fromList([8, 7])
        >>> tail, target = head, head.next
        >>> point = s.insertion_point(head, tail, target)
        >>> point is None
        True
        >>> head = LinkedList.fromList([2, 3, 1])
        >>> tail, target = head, head.next.next
        >>> point = s.insertion_point(head, tail, target)
        >>> point is None
        True
        >>> head = LinkedList.fromList([1, 2, 3, 7, 9, 13, 4])
        >>> tail = head.next.next.next.next.next
        >>> target = tail.next
        >>> p = s.insertion_point(head, tail, target)
        >>> p.val
        3
        """

        if head is None and tail is None:
            return None

        if target.val < head.val:
            return None
        elif target.val >= tail.val:
            return tail
        else:
            smaller = None
            node = head
            while node != target:
                if node.val <= target.val:
                    smaller = node
                node = node.next
            return smaller

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> result = s.insertionSortList(LinkedList.fromList([1]))
        >>> LinkedList.toList(result)
        [1]
        >>> result = s.insertionSortList(LinkedList.fromList([3, 7]))
        >>> LinkedList.toList(result)
        [3, 7]
        >>> result = s.insertionSortList(LinkedList.fromList([8, 7]))
        >>> LinkedList.toList(result)
        [7, 8]
        >>> result = s.insertionSortList(LinkedList.fromList([3, 2, 1]))
        >>> LinkedList.toList(result)
        [1, 2, 3]
        >>> result = s.insertionSortList(LinkedList.fromList([3, 2, 1, 7, 9, 13, 4]))
        >>> LinkedList.toList(result)
        [1, 2, 3, 4, 7, 9, 13]
        >>> result = s.insertionSortList(LinkedList.fromList([-84,142,41,-17,-71,170,186,183,-21,-76,76,10,29,81,112,-39,-6,-43,58,41,111,33,69,97,-38,82,-44,-7,99,135,42,150,149,-21,-30,164,153,92,180,-61,99,-81,147,109,34,98,14,178,105,5,43,46,40,-37,23,16,123,-53,34,192,-73,94,39,96,115,88,-31,-96,106,131,64,189,-91,-34,-56,-22,105,104,22,-31,-43,90,96,65,-85,184,85,90,118,152,-31,161,22,104,-85,160,120,-31,144,115]))
        >>> LinkedList.toList(result)
        [-96, -91, -85, -85, -84, -81, -76, -73, -71, -61, -56, -53, -44, -43, -43, -39, -38, -37, -34, -31, -31, -31, -31, -30, -22, -21, -21, -17, -7, -6, 5, 10, 14, 16, 22, 22, 23, 29, 33, 34, 34, 39, 40, 41, 41, 42, 43, 46, 58, 64, 65, 69, 76, 81, 82, 85, 88, 90, 90, 92, 94, 96, 96, 97, 98, 99, 99, 104, 104, 105, 105, 106, 109, 111, 112, 115, 115, 118, 120, 123, 131, 135, 142, 144, 147, 149, 150, 152, 153, 160, 161, 164, 170, 178, 180, 183, 184, 186, 189, 192]
        """
        if head is None:
            return None

        tail = head
        current = head.next
        while current:
            succeeding = current.next

            smaller = self.insertion_point(head, tail, current)

            if smaller is None:
                tail.next = current.next
                current.next = head
                head = current
            elif smaller == tail:
                tail = current
            else:
                tail.next = current.next
                current.next = smaller.next
                smaller.next = current
            current = succeeding

        return head

