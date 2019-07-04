# -*- coding: utf-8 -*-


code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


class Solution:
    def morse_encode(self, word):
        result = ""
        for char in word:
            result = result + code[ord(char) - ord('a')]
        return result

    def uniqueMorseRepresentations(self, words):
        combine = set()
        for word in words:
            encode = self.morse_encode(word)
            combine.add(encode)

        # print(combine)
        return len(combine)


if __name__ == '__main__':
    s = Solution()
    r = s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    assert r == 2
