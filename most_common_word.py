# -*- coding: utf-8 -*-


class Solution:
    def mostCommonWord(self, paragraph, banned):
        count = {}
        result, maximum = "", 0

        p = ""
        for char in paragraph:
            if char in (["!", "?", "'", ",", ";", "."]):
                p = p + " "
            else:
                p = p + char.lower()
        p = p.strip()
        for word in p.split(" "):
            if word == "":
                continue
            count[word] = count.get(word, 0) + 1
            if count[word] > maximum and word not in banned:
                maximum = count[word]
                result = word

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print(r)
    assert r == "ball"

    r = s.mostCommonWord("     Bob hit a ball, the hit BALL flew far!after,it was, ,,, ! hit...", ["hit"])
    print(r)
    assert r == "ball"
