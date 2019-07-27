# -*- coding: utf-8 -*-


class Solution:
    def strStr(self, haystack, needle):
        length1, length2 = len(haystack), len(needle)
        if length2 > length1:
            return -1
        elif length2 == 0:
            return 0

        for index, char in enumerate(haystack):
            if char == needle[0]:
                if haystack[index: index + length2] == needle:
                    return index

        return -1


if __name__ == '__main__':
    s = Solution()
    r = s.strStr("apple", "app")
    assert r == 0

    r = s.strStr("apple", "p")
    assert r == 1

    r = s.strStr("apple", "l")
    assert r == 3

    r = s.strStr("hello", "ll")
    assert r == 2

    r = s.strStr("aaaaa", "bba")
    assert r == -1

    # 一次遍历是 search 不出来的，需要回溯，这样子就可以写正则表达式了
    #
    r = s.strStr("mississippi", "issip")
    print(r)
    assert r == 4

    r = s.strStr("a", "")
    assert r == 0

    r = s.strStr("", "a")
    print(r)
    assert r == -1
