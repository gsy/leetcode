# -*- coding: utf-8 -*-


class Solution:
    def same_pattern(self, word, pattern):
        length1, length2 = len(word), len(pattern)
        if length1 != length2:
            return False

        mapping, seen = {}, set()
        for index, p in enumerate(pattern):
            current = mapping.get(p, None)
            if current is None:
                if word[index] in seen:
                    return False
                mapping[p] = word[index]
            elif current != word[index]:
                return False
            seen.add(word[index])
        return True

    def findAndReplacePattern(self, words, pattern):
        result = []
        for word in words:
            if self.same_pattern(word, pattern):
                result.append(word)

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")
    print(r)
    assert r == ["mee", "aqq"]
