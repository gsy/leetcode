# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.thousands = {"": 0, "M": 1, "MM": 2, "MMM": 3}
        self.hundreds = {"": 0, "C": 1, "CC": 2, "CCC": 3, "CD": 4, "D": 5, "DC": 6, "DCC": 7, "DCCC": 8, "CM": 9}
        self.tens = {"": 0, "X": 1, "XX": 2, "XXX": 3, "XL": 4, "L": 5, "LX": 6, "LXX": 7, "LXXX": 8, "XC": 9}
        self.digits = {"": 0, "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}

    def romanToInt(self, s):
        length = len(s)
        if length == 0:
            return 0

        result = [0, 0, 0, 0]
        mappings = [self.thousands, self.hundreds, self.tens, self.digits]
        string = ""
        for char in s:
            string = string + char
            decode = False
            for index, mapping in enumerate(mappings):
                if string in mapping:
                    result[index] = mapping[string]
                    decode = True
            if not decode:
                string = "" + char
                for index, mapping in enumerate(mappings):
                    if string in mapping:
                        result[index] = mapping[string]

        return 1000 * result[0] + 100 * result[1] + 10 * result[2] + result[3]





if __name__ == "__main__":
    s = Solution()
    r = s.romanToInt("")
    assert r == 0

    r = s.romanToInt("I")
    print(r)
    assert r == 1

    r = s.romanToInt("III")
    print(r)
    assert r == 3

    r = s.romanToInt("X")
    assert r == 10

    r = s.romanToInt("IV")
    assert r == 4

    r = s.romanToInt("IX")
    assert r == 9

    r = s.romanToInt("LVIII")
    assert r == 58

    r = s.romanToInt("MCMXCIV")
    print(r)
    assert r == 1994

    r = s.romanToInt("DCXXI")
    assert r == 621

    r = s.romanToInt("MDL")
    print(r)
    assert r == 1550
