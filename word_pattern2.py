# -*- coding: utf-8 -*-


class Solution:
    def wordPattern(self, pattern, string):
        words = [item for item in string.split(" ") if item]
        length1, length2 = len(pattern), len(words)
        if length1 != length2:
            return False

        mapping, seen = {}, set()
        for i in range(length1):
            word = words[i]
            if word in mapping:
                if mapping[word] != pattern[i]:
                    return False
            else:
                if pattern[i] in seen:
                    return False
                mapping[word] = pattern[i]
                seen.add(pattern[i])
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.wordPattern("abba", "dog cat cat dog")
    assert r is True

    r = s.wordPattern("abba", "dog cat cat fish")
    assert r is False

    r = s.wordPattern("aaaa", "dog cat cat dog")
    assert r is False

    r = s.wordPattern("aaaa", "dog dog dog dog")
    assert r is True

    r = s.wordPattern("abba", "dog dog dog dog")
    assert r is False

    r = s.wordPattern("aaaf", "dog dog dog dog")
    assert r is False
