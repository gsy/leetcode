__author__ = 'guang'

from linklist import LinkedList

class Solution(object):
    def length(self, head):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3])
        >>> s.length(head)
        3
        >>> s.length(None)
        0
        """
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        return count

    def kth(self, head, k):
        """
        >>> s = Solution()
        >>> head = LinkedList.fromList([1, 2, 3, 4, 5])
        >>> result = s.kth(head, 1)
        >>> result.val
        1
        >>> result = s.kth(head, 3)
        >>> result.val
        3
        >>> result = s.kth(head, 5)
        >>> result.val
        5
        >>> result = s.kth(head, 10)
        >>> result is None
        True
        """
        if head is None:
            return None

        count = 1
        node = head
        while node and count < k:
            count += 1
            node = node.next

        return node

    def isRecursivePalindrome(self, left, n, right, m, length):
        if n + m < length + 1:
            return self.isRecursivePalindrome(left.next, n + 1, right, m, length) and \
                   self.isRecursivePalindrome(left, n, right.next, m + 1, length)

        elif n + m == length + 1:
            if left.val != right.val:
                return False
            else:
                return True
        else:
            return False

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
        """
        if head is None:
            return False

        length = self.length(head)

        if length == 1:
            return True

        if length % 2 == 0:
            m = length / 2 + 1
            right = self.kth(head, m)
        else:
            m = length / 2 + 2
            right = self.kth(head, m)

        return self.isRecursivePalindrome(head, 1, right, m, length)

