# -*- coding: utf-8 -*-


class Solution:
    def word_count(self, word):
        result = {}
        for char in word:
            result[char] = result.get(char, 0) + 1
        return result

    def get_value(self, item):
        return item[1]

    def frequencySort(self, string):
        count = self.word_count(string)
        words = sorted(count.items(), key=self.get_value, reverse=True)
        result = ""
        for item in words:
            result = result + item[0] * item[1]
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.frequencySort("tree")
    assert r == "eert" or r == "eetr"

    r = s.frequencySort("cccaaa")
    print(r)
    assert r == "cccaaa" or r == "aaaccc"

    r = s.frequencySort("Aabb")
    print(r)
    assert r == "bbaA" or r == "bbAa"
