# -*- coding: utf-8 -*-

from greatest_common_divisor_of_strings import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.gcdOfStrings("Hello", "World")
    print(r)

    r = s.gcdOfStrings("ABCABC", "ABC")
    print(r)

    r = s.gcdOfStrings("ABABAB", "ABAB")
    print(r)

    r = s.gcdOfStrings("ABABAB", "")
    print(r)

    r = s.gcdOfStrings("ABABABC", "AB")
    print(r)
