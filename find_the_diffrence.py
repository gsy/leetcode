# -*- coding: utf-8 -*-


class Solution:
    def word_count(self, word):
        count = {}
        for char in word:
            count[char] = count.get(char, 0) + 1
        return count

    def findTheDifference(self, s, t):
        a = self.word_count(s)
        b = self.word_count(t)

        for key, value in b.items():
            if value - a.get(key, 0) > 0:
                return key

        return ""


if __name__ == '__main__':
    s = Solution()
    r = s.findTheDifference("abcd", "abced")
    assert r == "e"
