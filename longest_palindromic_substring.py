__author__ = 'guang'

class Solution(object):
    def common_length(self, left, right, s):
        length = len(s)
        result = 0
        while left >= 0 and right < length and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1

        return result

    def palindrome(self, s, index):
        """
        :param s:
        :param index:
        :return:

        >>> s = Solution()
        >>> text = "abcba"
        >>> s.palindrome(text, 1)
        (1, 1)
        >>> s.palindrome(text, 2)
        (0, 4)
        >>> text = "abba"
        >>> s.palindrome(text, 0)
        (0, 0)
        >>> s.palindrome(text, 1)
        (1, 1)
        >>> s.palindrome(text, 2)
        (2, 2)
        >>> s.palindrome(text, 3)
        (3, 3)
        >>> s.palindrome("a", 0)
        (0, 0)
        """
        left = index - 1
        right = index + 1
        common = self.common_length(left, right, s)

        return index - common, index + common

    def palindrome2(self, s, left, right):
        """

        :param s:
        :param lindex:
        :param rindex:
        :return:
        >>> s = Solution()
        >>> text = "abba"
        >>> s.palindrome2(text, 0, 1)
        (0, 0)
        >>> s.palindrome2(text, 1, 2)
        (0, 3)
        >>> s.palindrome2(text, 2, 3)
        (0, 0)
        """
        if s[left] != s[right]:
            return 0, 0

        common = self.common_length(left - 1, right + 1, s)

        return left - common, right + common

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        >>> s = Solution()
        >>> s.longestPalindrome("a")
        'a'
        >>> s.longestPalindrome("abccba")
        'abccba'
        >>> s.longestPalindrome("abbc")
        'bb'
        >>> text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        >>> s.longestPalindrome(text)
        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        """

        max_length = -1
        upper_limit = 1000
        result = (0, 0)
        for index in range(len(s)-1):
            palindrome1 = self.palindrome(s, index)
            palindrome2 = self.palindrome2(s, index, index+1)
            length1 = palindrome1[1] - palindrome1[0]
            length2 = palindrome2[1] - palindrome2[0]

            if length1 > max_length:
                max_length = length1
                result = palindrome1
                if max_length >= upper_limit:
                    break

            if length2 > max_length:
                max_length = length2
                result = palindrome2
                if max_length >= upper_limit:
                    break

        return s[result[0]:result[1]+1]
