# -*- coding: utf-8 -*-

from count_and_say2 import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.countAndSay(1)
    print(r)

    r = s.countAndSay(3)
    print(r)

    r = s.do_count_and_say("21")
    print(r)

    r = s.countAndSay(5)
    print(r)

    r = s.countAndSay(6)
    print(r)

    r = s.countAndSay(7)
    print(r)
