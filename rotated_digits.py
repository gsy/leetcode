# -*- coding: utf-8 -*-

class Solution:
    def rotate(self, char):
        return {
            '0': '0',
            '1': '1',
            '8': '8',
            '2': '5',
            '5': '2',
            '6': '9',
            '9': '6'
        }.get(char, None)

    def is_good_number(self, num):
        new_number = ''
        for char in str(num):
            rotated = self.rotate(char)
            if rotated is None:
                return False
            else:
                new_number = new_number + rotated
        return int(new_number) != num

    def rotatedDigits(self, N):
        count = 0
        for num in range(1, N+1):
            if self.is_good_number(num):
                count = count + 1
        return count

if __name__ == "__main__":
    s = Solution()
    r = s.rotatedDigits(10)
    assert r == 4

    r = s.rotatedDigits(30)
    print(r)
    assert r == 15

    r = s.rotatedDigits(2)
    print(r)
    assert r == 1
