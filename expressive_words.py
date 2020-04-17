# -*- coding: utf-8 -*-


class Solution:
    def stretchy(self, word, string):
        # word -> string
        index, prev, count, stretch, length = 0, None, 0, False, len(word)
        for char in string:
            if index < length and char == word[index]:
                if stretch and count < 3:
                    return False
                stretch = False
                index = index + 1
                if char == prev:
                    count = count + 1
                else:
                    count = 1
                prev = char
            else:
                if prev and char == prev:
                    stretch = True
                    count = count + 1
                else:
                    return False

        if stretch:
            return count >= 3 and index == length
        else:
            return index == length

    def expressiveWords(self, string, words):
        result = 0
        for word in words:
            if self.stretchy(word, string):
                # print(word, string)
                result = result + 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.expressiveWords("heeellooo", words=["hello", "hi", "helo"])
    assert r == 1

    r = s.expressiveWords("heellooo", words=["hello"])
    assert r == 0

    r = s.expressiveWords("heeelloo", words=["hello"])
    assert r == 0

    r = s.expressiveWords("dddiiiinnssssssoooo", ["dinnssoo"])
    assert r == 1

    r = s.expressiveWords("dddiiiinnssssssoooo", ["ddiinnso"])
    assert r == 1

    r = s.expressiveWords("dddiiiinnssssssoooo", ["dinnssoo", "ddinso", "ddiinnso", "ddiinnssoo", "ddiinso", "dinsoo", "ddiinsso", "dinssoo", "dinso"])
    assert r == 3
