# -*- coding: utf-8 -*-


class Solution:
    def is_substring(self, pattern, string):
        if string == pattern:
            return True
        elif string == "" or pattern == "":
            return False

        length_pattern = len(pattern)
        length_string = len(string)
        if length_pattern > length_string:
            return False

        for index, char in enumerate(pattern):
            if char != string[index]:
                return False
        return True

    def repeatedSubstringPattern(self, s):
        length = len(s)
        if length <= 1:
            return False

        if length % 2 == 0:
            half = int(length/2)
            if (s[half:] == s[:half]):
                return True

        pattern, pattern_length = "", 0
        while pattern_length <= int(length / 2):
            pattern_length = pattern_length + 1
            remain = length - pattern_length
            pattern = s[remain:]
            if remain % 2 == 0:
                half = int(remain/2)
                left, right = s[0:half], s[half:remain]
                if left == right and self.is_substring(pattern, left):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()

    r = s.repeatedSubstringPattern("")
    assert r is False

    r = s.repeatedSubstringPattern("a")
    assert r is False

    r = s.repeatedSubstringPattern("ab")
    assert r is False

    r = s.repeatedSubstringPattern("aa")
    assert r is True

    r = s.repeatedSubstringPattern("abc")
    assert r is False

    r = s.repeatedSubstringPattern("abcab")
    assert r is False

    r = s.repeatedSubstringPattern("abcabc")
    assert r is True

    r = s.is_substring("abc", "abc")
    assert r is True

    r = s.repeatedSubstringPattern("abcabcabc")
    assert r is True

    r = s.repeatedSubstringPattern("ababab")
    assert r is True

    r = s.repeatedSubstringPattern("aabaaba")
    assert r is False
