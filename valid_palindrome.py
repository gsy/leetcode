__author__ = 'guang'

class Solution(object):
    def palindrome(self, s):
        """

        :param s:
        :return:
        >>> s = Solution()
        >>> s.palindrome("A")
        True
        >>> s.palindrome("")
        True
        """
        if len(s) == 0:
            return True

        i, j = 0, len(s) - 1

        while i < j:
            if not s[i] == s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        >>> s = Solution()
        >>> s.isPalindrome("A man, a plan, a canal: Panama")
        True
        >>> s.isPalindrome("race a car")
        False
        >>> s.isPalindrome("")
        True
        >>> s.isPalindrome("0P")
        False
        """
        words = []
        for c in s:
            if c.isalnum():
                words.append(c.lower())

        return self.palindrome(words)


