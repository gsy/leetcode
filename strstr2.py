# -*- coding: utf-8 -*-


class Solution:
    def pattern_generator(self, needle):
        for char in needle:
            yield char

    def strStr(self, haystack, needle):
        length = len(needle)
        if length == 0:
            return 0

        state = "search"
        patterns = self.pattern_generator(needle)
        pattern = next(patterns)
        result = 0
        for index, char in enumerate(haystack):
            try:
                if state == "search":
                    if char == pattern:
                        result = index
                        state = "match"
                        pattern = next(patterns)

                elif state == "match":
                    if char == pattern:
                        pattern = next(patterns)
                    else:
                        result = 0
                        state = "search"
                        patterns = self.pattern_generator(needle)
                        pattern = next(patterns)
            except StopIteration:
                print(state, pattern)
                if state == "match":
                    return result
                else:
                    # char 也需要回溯到上一个版本
                    result = 0
                    state = "search"
                    patterns = self.pattern_generator(needle)
                    pattern = next(patterns)
        return -1


if __name__ == '__main__':
    s = Solution()
    # r = s.strStr("apple", "app")
    # assert r == 0

    # r = s.strStr("apple", "p")
    # assert r == 1

    # r = s.strStr("apple", "l")
    # assert r == 3

    # r = s.strStr("hello", "ll")
    # assert r == 2

    # r = s.strStr("aaaaa", "bba")
    # assert r == -1

    # 一次遍历是 search 不出来的，需要回溯，这样子就可以写正则表达式了
    #
    r = s.strStr("mississippi", "issip")
    print(r)
    assert r == 4
