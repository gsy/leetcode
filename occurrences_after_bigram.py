# -*- coding: utf-8 -*-

class Solution:
    def findOcurrences(self, text, first, second):
        result, words = [], text.split(" ")
        for i in range(len(words)-2):
            if words[i] == first and words[i+1] == second:
                result.append(words[i+2])
        return result

if __name__ == "__main__":
    s = Solution()
    r = s.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good")
    print(r)
    assert r == ["girl", "student"]

    r = s.findOcurrences(text = "we will we will rock you", first="we", second="will")
    print(r)
    assert r == ["we", "rock"]
