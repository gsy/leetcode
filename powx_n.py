# -*- coding: utf-8 -*-


class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)

        powers = [1, x]

        power_index = 2
        power = x
        while power_index <= n:
            power = power * power
            power_index = power_index * 2
            powers.append(power)

        # print(powers)

        result = 1
        index = 1
        mask = 1
        while mask <= n:
            if (mask & n):
                result = result * powers[index]
            mask = mask << 1
            index = index + 1

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.myPow(10, 0)
    assert r == 1

    r = s.myPow(10, 1)
    assert r == 10

    r = s.myPow(99999, 0)
    assert r == 1

    r = s.myPow(2, 10)
    print(r)
    assert r == 1024

    r = s.myPow(3, 10)
    print(r)
    assert r == 59049

    r = s.myPow(2.10000, 3)
    print(r)
    assert r - 9.261 <= 0.00001

    r = s.myPow(2.00000, 2)
    print(r)
    assert r == 4.0

    r = s.myPow(2.00000, -2)
    print(r)
    assert abs(r - 0.25000) <= 0.00001
