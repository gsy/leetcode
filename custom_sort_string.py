# -*- coding: utf-8 -*-


class Solution:
    def get_weights(self, sort_by):
        result = {}
        for index, char in enumerate(sort_by):
            result[char] = index
        return result

    def compare(self, a):
        return self.weights.get(a, self.weights_length)

    def customSortString(self, sort_by, text):
        self.weights = self.get_weights(sort_by)
        self.weights_length = len(self.weights)
        return "".join(sorted(text, key=self.compare))


if __name__ == '__main__':
    s = Solution()
    r = s.customSortString("cba", "abcd")
    print(r)
    assert r == "cbad"
