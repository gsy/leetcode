__author__ = 'guang'

from linklist import LinkedList

class Solution(object):
    def middle_and_length(self, head):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> middle, length = s.middle_and_length(head)
        >>> length
        3
        >>> middle.val
        2
        >>> middle, length = s.middle_and_length(None)
        >>> length
        0
        >>> middle, length = s.middle_and_length(LinkedList.fromList([1]))
        >>> length
        1
        >>> middle.val
        1
        >>> head = LinkedList.fromList([1, 2])
        >>> middle, length = s.middle_and_length(head)
        >>> middle.val == 1 and length == 2
        True
        >>> head = LinkedList.fromList([1, 2, 3, 4])
        >>> middle, length = s.middle_and_length(head)
        >>> middle.val == 2 and length == 4
        True
        """
        if head is None:
            return None, 0

        slower = head
        faster = head.next
        count = 1
        while faster:
            count += 1
            faster = faster.next
            if faster is None:
                return slower, count
            count += 1
            faster = faster.next
            slower = slower.next

        return slower, count

    def isRecursivePalindrome(self, left, lindex, right, rindex, length):

        if lindex + rindex == length + 1:
            return left.val == right.val, right

        elif lindex + rindex < length + 1:
            result, end = self.isRecursivePalindrome(left.next, lindex + 1, right, rindex, length)
            right = end.next
            if result:
                return left.val == right.val, right
            else:
                return False, right

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        >>> s = Solution()
        >>> s.isPalindrome(None)
        False
        >>> head = LinkedList.fromList([1])
        >>> s.isPalindrome(head)
        True
        >>> head = LinkedList.fromList([1, 3, 1])
        >>> s.isPalindrome(head)
        True
        >>> head = LinkedList.fromList([1, 3])
        >>> s.isPalindrome(head)
        False
        >>> head = LinkedList.fromList([1, 2, 3, 2, 1])
        >>> s.isPalindrome(head)
        True
        >>> head = LinkedList.fromList([1, 2, 2, 1])
        >>> s.isPalindrome(head)
        True
        >>> head = LinkedList.fromList([1, 2, 3, 8, 7, 2, 1])
        >>> s.isPalindrome(head)
        False
        """
        if head is None:
            return True

        middle, length = self.middle_and_length(head)

        if length == 1:
            return True

        lindex = 1
        if length % 2 == 0:
            rindex = length / 2 + 1
        else:
            rindex = length / 2 + 2
        right = middle.next

        return self.isRecursivePalindrome(head, lindex, right, rindex, length)[0]

