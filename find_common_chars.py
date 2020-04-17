# -*- coding: utf-8 -*-


class Solution:
    def chars(self, word):
        result = {}
        for char in word:
            if char in result:
                result[char] = result[char] + 1
            else:
                result[char] = 1
        return result

    def find_common(self, a, b):
        result = {}
        for key in b:
            if key in a:
                result[key] = min(a[key], b[key])
        return result

    def commonChars(self, words):
        if len(words) == 0:
            return []

        common = None
        for word in words:
            current = self.chars(word)
            if common is None:
                common = current
            else:
                common = self.find_common(common, current)

        result = []
        for key, value in common.items():
            for i in range(value):
                result.append(key)

        return result
