# -*- coding: utf-8 -*-

import string

class Solution:
    def word_count(self, word):
        result = {}
        for char in word:
            char = char.lower()
            if char in string.ascii_lowercase:
                result[char] = result.get(char, 0) + 1
        return result

    def contains(self, current, words):
        for key, value in words.items():
            if key not in current or current[key] < value:
                return False
        return True

    def shortestCompletingWord(self, licensePlate, words):
        words = sorted(words, key=len)

        license_wordcount = self.word_count(licensePlate)
        for word in words:
            current = self.word_count(word)
            if self.contains(current, license_wordcount):
                return word
        return None

if __name__ == "__main__":
    s = Solution()
    r = s.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"])
    assert r == "steps"

    r = s.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"])
    print(r)
    assert r == "pest"
