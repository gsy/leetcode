# -*- coding: utf-8 -*-


class Solution:
    def is_prime(self, num):
        return num in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)

    def get_bits(self, num):
        mask = 1
        count = 0
        while num >= mask:
            if num & mask:
                count = count + 1
            mask = mask << 1
        return count

    def countPrimeSetBits(self, L: int, R: int) -> int:
        result = 0
        for num in range(L, R+1):
            bits = self.get_bits(num)
            if self.is_prime(bits):
                result = result + 1

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.countPrimeSetBits(6, 10)
    assert r == 4

    r = s.is_prime(4)
    assert r is False

    r = s.countPrimeSetBits(10, 15)
    print(r)
    assert r == 5

    r = s.countPrimeSetBits(501808, 507373)
    print(r)
    assert r == 2231
