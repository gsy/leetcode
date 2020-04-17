# -*- coding: utf-8 -*-

from first_bad_version import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.firstBadVersion(5)
    print(r)

    r = s.firstBadVersion(3)
    print(r)

    r = s.firstBadVersion(10)
    print(r)

    r = s.firstBadVersion(100)
    print(r)

    r = s.firstBadVersion(0)
    print(r)
