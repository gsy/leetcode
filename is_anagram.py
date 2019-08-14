# -*- coding: utf-8 -*-


class Solution:
    def word_count(self, word):
        count = {}
        for char in word:
            count[char] = count.get(char, 0) + 1
        return count

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count_s = self.word_count(s)
        count_t = self.word_count(t)

        for key, value in count_s.items():
            if value != count_t.get(key, 0):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isAnagram("anagram", "nagaram")
    assert r is True

    r = s.isAnagram("rat", "car")
    assert r is False
