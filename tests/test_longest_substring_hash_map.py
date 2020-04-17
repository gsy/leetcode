# -*- coding: utf-8 -*-

from longest_substring_hash_map import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLongestSubstring("abcabcbb")
    print(r)
    assert r == 3

    r = s.lengthOfLongestSubstring("bbb")
    print(r)
    assert r == 1

    r = s.lengthOfLongestSubstring("pwwkew")
    print(r)
    assert r == 3

    r = s.lengthOfLongestSubstring("abcdefgh")
    print(r)
    assert r == 8

    r = s.lengthOfLongestSubstring("dvdf")
    print(r)
    assert r == 3

    r = s.lengthOfLongestSubstring("abba")
    print(r)
    assert r == 2

    r = s.lengthOfLongestSubstring("tmmzuxt")
    print(r)
    assert r == 5

    r = s.lengthOfLongestSubstring("biidygcc")
    print(r)
    assert r == 5

    r = s.lengthOfLongestSubstring("wobgrovw")
    print(r)
    assert r == 6
