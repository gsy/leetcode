# -*- coding: utf-8 -*-


class Solution:
    def replace(self, word):
        if len(word) == 0:
            return ""

        initial = word[0].lower()
        if initial in ('a', 'e', 'i', 'o', 'u'):
            return word + "ma"
        else:
            return word[1:] + word[0] + "ma"

    def toGoatLatin(self, string):
        words = string.split(' ')
        result = []
        for index, word in enumerate(words):
            result.append(self.replace(word) + "a" * (index + 1))

        return " ".join(result)


if __name__ == '__main__':
    s = Solution()
    r = s.toGoatLatin("I speak Goat Latin")
    print(r)
    assert r == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    r = s.toGoatLatin("The quick brown fox jumped over the lazy dog")
    print(r)
    assert r == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
