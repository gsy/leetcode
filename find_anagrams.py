# -*- coding: utf-8 -*-


class Solution:
    def word_count(self, word):
        result = {}
        for char in word:
            result[char] = result.get(char, 0) + 1
        return result

    def equal(self, current, words):
        for key, value in words.items():
            if key not in current or current[key] != value:
                return False
        return True

    def findAnagrams(self, s, p):
        # 滑动窗口，窗口的大小固定？
        # 滑动的过程中只要计算　left, right 的变化值
        lens, lenp = len(s), len(p)
        if lens < lenp:
            return []

        current, result = {}, []
        words = self.word_count(p)
        for left in range(0, lens - lenp + 1):
            right = left + lenp - 1
            if left == 0:
                for i in range(left, left + lenp):
                    char = s[i]
                    current[char] = current.get(char, 0) + 1
            else:
                current[s[left-1]] = current[s[left - 1]] - 1
                current[s[right]] = current.get(s[right], 0) + 1
            # print(left, current)
            if self.equal(current, words):
                result.append(left)
        return result


if __name__ == "__main__":
    s = Solution()
    r = s.findAnagrams("cbaebabacd", "abc")
    print(r)
    assert r == [0, 6]

    r = s.findAnagrams("abab", "ab")
    print(r)
    assert r == [0, 1, 2]
