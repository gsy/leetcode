# -*- coding: utf-8 -*-


class Solution:
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        return max(len(a), len(b))


if __name__ == '__main__':
    s = Solution()
    r = s.findLUSlength("aba", "cdc")
    print(r)
    assert r == 3

    r = s.findLUSlength("hello", "halo")
    print(r)
    assert r == 5

    r = s.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef")
    print(r)
    assert r == 17

    r = s.findLUSlength("horbxeemlgqpqbujbdagizcfairalg", "iwvtgyojrfhyzgyzeikqagpfjoaeen")
    print(r)
    assert r == 30
