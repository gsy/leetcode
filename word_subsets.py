# -*- coding: utf-8 -*-


class Solution:
    def word_count(self, word):
        count = {}
        for char in word:
            count[char] = count.get(char, 0) + 1
        return count

    def all_is_subset(self, sets, word):
        target = self.word_count(word)
        sources = [self.word_count(item) for item in sets]
        # print(target, sources)
        for source in sources:
            for key, value in source.items():
                if target.get(key, 0) < value:
                    return False
        return True

    def wordSubsets(self, words, sets):
        result = []
        for word in words:
            if self.all_is_subset(sets, word):
                result.append(word)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"])
    assert r == ["facebook", "google", "leetcode"]

    r = s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"])
    assert r == ["apple", "google", "leetcode"]

    r = s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"])
    assert r == ["facebook", "google"]

    r = s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"])
    assert r == ["google", "leetcode"]

    r = s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["ec", "oc", "ceo"])
    assert r == ["facebook", "leetcode"]
