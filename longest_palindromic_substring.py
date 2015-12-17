__author__ = 'guang'

class Solution(object):
    def common(self, s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            return ""

        if s1[0] == s2[0]:
            return s1[0] + self.common(s1[1:], s2[1:])
        else:
            return ""

    def palindrome(self, s, index):
        """
        :param s:
        :param index:
        :return:

        >>> s = Solution()
        >>> text = "abcba"
        >>> s.palindrome(text, 0)
        'a'
        >>> s.palindrome(text, 1)
        'b'
        >>> s.palindrome(text, 2)
        'abcba'
        >>> text = "abba"
        >>> s.palindrome(text, 0)
        'a'
        >>> s.palindrome(text, 1)
        'b'
        >>> s.palindrome(text, 2)
        'b'
        >>> s.palindrome(text, 3)
        'a'
        """
        left = s[:index]
        right = s[index+1:]
        minLength = min(len(left), len(right))
        left = left[len(left)-minLength:]
        right = right[:minLength]

        common_part = self.common(left, right[::-1])
        return common_part + s[index] + common_part[::-1]

    def palindrome2(self, s, lindex, rindex):
        """

        :param s:
        :param lindex:
        :param rindex:
        :return:
        >>> s = Solution()
        >>> text = "abba"
        >>> s.palindrome2(text, 0, 1)
        ''
        >>> s.palindrome2(text, 1, 2)
        'abba'
        >>> s.palindrome2(text, 2, 3)
        ''
        """
        if s[lindex] != s[rindex]:
            return ''

        left = s[:lindex]
        right = s[rindex+1:]
        minLength = min(len(left), len(right))
        left = left[len(left)-minLength:]
        right = right[:minLength]

        common_part = self.common(left, right[::-1])
        return common_part + s[lindex] + s[rindex] + common_part[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        >>> s = Solution()
        >>> s.longestPalindrome("abccba")
        'abccba'
        >>> s.longestPalindrome("abbc")
        'bb'
        """

        if len(s) <= 1:
            return ''

        max_length = 0
        result = ""
        for index in range(1, len(s)-1):
            palindrome1 = self.palindrome(s, index)
            palindrome2 = self.palindrome2(s, index, index+1)
            length1 = len(palindrome1)
            length2 = len(palindrome2)

            if length1 > max_length:
                max_length = length1
                result = palindrome1

            if length2 > max_length:
                max_length = length2
                result = palindrome2

        return result