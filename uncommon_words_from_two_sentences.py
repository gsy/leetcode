# -*- coding: utf-8 -*-

class Solution:
    def words_set(self, words):
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return [key for key,value in word_count.items() if value == 1]

    def uncommonFromSentences(self, a, b):
        return self.words_set(a.split(" ") + b.split(" "))


if __name__ == "__main__":
    s = Solution()
    r = s.uncommonFromSentences("this apple is sweet", "this apple is sour")
    print(r)
    assert r == ["sweet", "sour"]

    r = s.uncommonFromSentences("apple apple", "banana")
    print(r)
    assert r == ["banana"]

    r = s.uncommonFromSentences("s z z z s", "s z ejt")
    print(r)
    assert r == ["ejt"]
