# -*- coding: utf-8 -*-

class Solution:
    def word_count(self, word):
        result = {}
        for char in word:
            result[char] = result.get(char, 0) + 1
        return result

    def contains(self, current, words):
        for key, value in words.items():
            if key not in current or current[key] < value:
                return False
        return True


    def minWindow(self, s ,t):
        # 滑动窗口，先移动后边，然后移动左边
        left, right = 0, 0
        lens, lent = len(s), len(t)
        if lens < lent:
            return ""

        result, substring = "", ""
        current, words = {}, self.word_count(t)
        while right < lens:
            char = s[right]
            current[char] = current.get(char, 0) + 1
            right = right + 1
            if self.contains(current, words):
                while left < right and self.contains(current, words):
                    remove = s[left]
                    current[remove] = current[remove] - 1
                    left = left + 1
                substring = s[left-1: right]
            if len(result) == 0:
                result = substring
            elif len(result) > len(substring):
                result = substring
        return result

if __name__ == "__main__":
    s = Solution()
    r = s.minWindow("ADOBECODEBANC", "ABC")
    print(r)
