# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.thousands_mapping = {
            0: '',
            1: 'M',
            2: 'MM',
            3: 'MMM',
        }
        self.hundrends_mapping = {
            0: '',
            1: 'C',
            2: 'CC',
            3: 'CCC',
            4: 'CD',
            5: 'D',
            6: 'DC',
            7: 'DCC',
            8: 'DCCC',
            9: 'CM',
        }
        self.tens_mapping = {
            0: '',
            1: 'X',
            2: 'XX',
            3: 'XXX',
            4: 'XL',
            5: 'L',
            6: 'LX',
            7: 'LXX',
            8: 'LXXX',
            9: 'XC',
        }
        self.digits_mapping = {
            0: '',
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
        }

    def convert(self, numbers):
        thousands, hundrends, tens, digits = numbers
        return self.thousands_mapping[thousands] + \
            self.hundrends_mapping[hundrends] + \
            self.tens_mapping[tens] + \
            self.digits_mapping[digits]

    def intToRoman(self, num):
        numbers = [0, 0, 0, 0]
        index = 3
        while num > 0:
            numbers[index] = num % 10
            index = index - 1
            num = int(num / 10)
        return self.convert(numbers)


if __name__ == '__main__':
    s = Solution()
    r = s.intToRoman(1)
    assert r == 'I'

    r = s.intToRoman(11)
    assert r == 'XI'

    r = s.intToRoman(10)
    assert r == 'X'

    r = s.intToRoman(20)
    assert r == 'XX'

    r = s.intToRoman(28)
    assert r == 'XXVIII'

    r = s.intToRoman(128)
    assert r == 'CXXVIII'

    r = s.intToRoman(48)
    assert r == 'ILVIII'

    r = s.intToRoman(1994)
    assert r == 'MCMXCIV'
