# -*- coding: utf-8 -*-

import string

class Solution:
    def isValidChar(self, char):
        return char.lower() in string.ascii_lowercase + string.digits

    def isPalindrome(self, s):
        length = len(s)
        if length == 0:
            return True

        middle = length / 2
        left, right = 0, length - 1
        while left <= right:
            while not self.isValidChar(s[left]) and left < right:
                left = left + 1
            while not self.isValidChar(s[right]) and left < right:
                right = right - 1

            if left >= right:
                break

            if s[left].lower() != s[right].lower():
                return False
            else:
                left, right = left + 1, right - 1
        return True

if __name__ == "__main__":
    s = Solution()
    r = s.isPalindrome("A man, a plan, a canal: Panama")
    assert r is True

    r = s.isPalindrome("aba")
    assert r is True

    r = s.isPalindrome("abdba")
    assert r is True

    r = s.isPalindrome("abba")
    assert r is True

    r = s.isPalindrome("ab,,,   ba")
    assert r is True

    r = s.isPalindrome("ab,1ba")
    assert r is True

    r = s.isPalindrome("1ab,1ba")
    assert r is False

    r = s.isPalindrome("1ab,1ba1")
    assert r is True

    r = s.isPalindrome("race start")
    assert r is False

    r = s.isPalindrome("")
    assert r is True

    r = s.isPalindrome(" ")
    assert r is True
