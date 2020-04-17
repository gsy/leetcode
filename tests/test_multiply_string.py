# -*- coding: utf-8 -*-

from multiply_string import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.add("1234", "456")
    print(r)

    r = s.single_multiply("1234", "5")
    print(r)

    r = s.multiply("1234", "5")
    print(r)

    r = s.multiply("1234", "15")
    print(r)

    r = s.multiply("123", "456")
    print(r)

    r = s.multiply("52", "0")
    print(r, len(r))
