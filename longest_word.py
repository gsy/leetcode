# -*- coding: utf-8 -*-

class Solution:

    def longestWord(self, words):
        words = sorted(words, key=len)
        # print(words)

        prefix = set()
        result, maxlen = "", 0
        for word in words:
            length, flag = len(word), False
            if length == 1:
                prefix.add(word)
                flag = True
            else:
                substring = word[:-1]
                if substring in prefix:
                    flag = True
                    prefix.add(word)

            if flag:
                if length > maxlen:
                    result = word
                    maxlen = length
                elif length == len(result) and word < result:
                    result = word

        return result

if __name__ == "__main__":
    s = Solution()
    r = s.longestWord(["w", "wo", "wor", "worl", "world"])
    print(r)
    assert r == "world"

    r = s.longestWord( ["a", "banana", "app", "appl", "ap", "apply", "apple"])
    print(r)
    assert r == "apple"

    r = s.longestWord(["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"])
    assert r == "e"
