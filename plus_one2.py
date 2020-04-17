# -*- coding: utf-8 -*-

class Solution:
    def plusOne(self, digits):
        length = len(digits)
        carry, result = 0, []
        for i in range(length):
            index = length - i - 1
            if i == 0:
                plus = int(digits[index] + 1 + carry)
            else:
                plus = int(digits[index] + carry)
            plus, carry = plus % 10, int(plus / 10)
            result.append(plus)

        if carry:
            result.append(carry)
        return result[::-1]

if __name__ == "__main__":
    s = Solution()
    r = s.plusOne([])
    assert r == []

    r = s.plusOne([0])
    assert r == [1]

    r = s.plusOne([9])
    assert r == [1, 0]

    r = s.plusOne([8])
    assert r == [9]

    r = s.plusOne([1, 8])
    assert r == [1, 9]

    r = s.plusOne([9, 9])
    assert r == [1, 0, 0]

    r = s.plusOne([1, 2, 3])
    assert r == [1, 2, 4]
