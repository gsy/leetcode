# -*- coding: utf-8 -*-


class Solution:
    def is_vowels(self, char):
        return char.lower() in ['a', 'e', 'i', 'o', 'u']

    def reverseVowels(self, s):
        length = len(s)
        if length <= 1:
            return s

        left, right = "", ""
        start, end = 0, length - 1

        while start < end:
            if self.is_vowels(s[start]):
                if self.is_vowels(s[end]):
                    left, right = left + s[end], s[start] + right
                    start, end = start + 1, end - 1
                else:
                    right = s[end] + right
                    end = end - 1
            else:
                if self.is_vowels(s[end]):
                    left = left + s[start]
                    start = start + 1
                else:
                    left, right = left + s[start], s[end] + right
                    start, end = start + 1, end - 1

        result = left + right
        if len(result) == length:
            return result
        else:
            return left + s[end] + right


if __name__ == '__main__':
    s = Solution()
    r = s.reverseVowels("hello")
    assert r == "holle"

    r = s.reverseVowels("leetcode")
    assert r == "leotcede"

    r = s.reverseVowels("a.")
    print(r)
    assert r == "a."

    r = s.reverseVowels("aabee")
    print(r)
    assert r == "eebaa"

    r = s.reverseVowels("aA")
    assert r == "Aa"
