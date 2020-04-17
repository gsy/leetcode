# -*- coding: utf-8 -*-

from string_compression import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.compress([])
    print(r)

    r = s.compress(["a", "a", "b"])
    print(r)

    r = s.compress(["a","a","b","b","c","c","c"])
    print(r)

    r = s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
    print(r)


    r = s.compress(["a","b","c"])
    print(r)
