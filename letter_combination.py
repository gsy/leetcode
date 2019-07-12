# -*- coding: utf-8 -*-


class Solution:
    def combine(self, a, b):
        for itema in a:
            for itemb in b:
                yield itema + itemb

    def combinations(self, arrays):
        length = len(arrays)
        if length == 0:
            return []
        elif length == 1:
            return arrays[0]
        else:
            a = arrays[0]
            for i in range(1, length):
                b = arrays[i]
                a = self.combine(a, b)

            return list(a)

    def __init__(self):
        self.mapping = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits):
        arrays = []
        for digit in digits:
            arrays.append(self.mapping[digit])

        return self.combinations(arrays)


if __name__ == '__main__':
    s = Solution()
    r = s.letterCombinations("2")
    print(r)
    assert r == ['a', 'b', 'c']

    r = s.letterCombinations("23")
    assert r == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    r = s.letterCombinations("234")
    assert r == combinations([], 3)
