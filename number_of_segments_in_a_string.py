# -*- coding: utf-8 -*-


class Solution:
    def countSegments(self, s):
        if s == '':
            return 0

        s = s.strip()
        return len([word for word in s.strip().split(' ') if len(word) > 0])


if __name__ == '__main__':
    s = Solution()
    r = s.countSegments(", , , ,        a, eaefa")
    assert r == 6

    r = s.countSegments("    ")
    assert r == 0

    r = s.countSegments("apple pie")
    assert r == 2
