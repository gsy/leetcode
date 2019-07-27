# -*- coding: utf-8 -*-


class Solution:
    def shift(self, char, times):
        diff = ord(char) - ord('a')
        return chr((diff + times) % 26 + ord('a'))

    def accumulations(self, shifts):
        total = sum(shifts)
        acc, result = 0, []
        for shift in shifts:
            result.append(total - acc)
            acc = acc + shift
        return result

    def shiftingLetters(self, string, shifts):
        shifts = self.accumulations(shifts)

        result = ""
        for index, char in enumerate(string):
            result = result + self.shift(char, shifts[index])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.shift('z', 1))

    r = s.shiftingLetters("abc", shifts=[3, 5, 9])
    print(r)
    assert r == "rpl"
