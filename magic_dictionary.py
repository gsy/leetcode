# -*- coding: utf-8 -*-

import string

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.origin = {}


    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        """
        for word in words:
            length = len(word)
            key = "{}/{}".format(length, word[0])
            ls = self.origin.get(key, [])
            ls.append(word)
            self.origin[key] = ls

    def only_modify_one_char(self, word, origin):
        count = 0
        for i, char in enumerate(word):
            if char != origin[i]:
                count = count + 1
            if count >= 2:
                return False
        return count == 1


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        length = len(word)
        if length == 1:
            for letter in string.ascii_lowercase:
                key = "{}/{}".format(1, letter)
                if key in self.origin and letter != word:
                    return True
            return False

        key = "{}/{}".format(len(word), word[0])
        ls = self.origin.get(key, [])
        if len(ls) == 0:
            return False

        for origin in ls:
            if self.only_modify_one_char(word, origin):
                return True
        return False


if __name__ == "__main__":
    obj = MagicDictionary()
    obj.buildDict(["hello", "leetcode"])
    r = obj.search("hello")
    assert r is False

    r = obj.search("hhllo")
    assert r is True

    r = obj.search("hell")
    assert r is False

    r = obj.search("leetcoded")
    assert r is False

    obj.buildDict(["a"])
    r = obj.search("a")
    assert r is False

    obj.buildDict(["a"])
    r = obj.search("b")
    assert r is True


#     ["MagicDictionary", "buildDict", "search", "search", "search", "search", "search", "search"]
# [[], [["a"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"]]
