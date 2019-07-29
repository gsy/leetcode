# -*- coding: utf-8 -*-


class Solution:
    def hashing(self, word):
        result = 1
        for i, char in enumerate(word):
            result = result * (ord(char) - ord('a') + 1)
        return result

    def findAnagrams(self, s, p):
        length_s, length_p = len(s), len(p)
        if length_s < length_p:
            return ""
        result = []

        standard = self.hashing(p)
        for i in range(length_s):
            if i + length_p > length_s:
                break
            current = self.hashing(s[i: i + length_p])
            if current == standard:
                result.append(i)

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.findAnagrams("cbaebabacd", "abc")
    # print(r)
    assert r == [0, 6]

    r = s.findAnagrams("abca", "abc")
    assert r == [0, 1]

    r = s.findAnagrams("abcab", "abc")
    assert r == [0, 1, 2]
