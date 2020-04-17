# -*- coding: utf-8 -*-


class Solution:
    def reverseWords(self, s):
        s = s.strip()
        ls = [item for item in s.split(' ') if item]
        return ' '.join(ls[::-1])


if __name__ == '__main__':
    s = Solution()
    r = s.reverseWords("the sky is blue")
    assert r == "blue is sky the"

    r = s.reverseWords("  hello world!  ")
    assert r == "world! hello"

    r = s.reverseWords("a good   example")
    assert r == "example good a"
