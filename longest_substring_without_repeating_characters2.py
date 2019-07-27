# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        left, right, length = 0, 0, len(s)
        result, chars_to_index = 0, {}
        while right < length:
            char = s[right]
            if char in chars_to_index and chars_to_index[char] >= left:
                left = chars_to_index[char] + 1
            chars_to_index[char] = right
            right = right + 1
            if right - left > result:
                result = right - left
        return result


if __name__ == "__main__":
    s = Solution()
    r = s.lengthOfLongestSubstring("abcabcbb")
    print(r)
    assert r == 3

    r = s.lengthOfLongestSubstring("bbbbbb")
    print(r)
    assert r == 1

    r = s.lengthOfLongestSubstring("pwwkew")
    print(r)
    assert r == 3

    r = s.lengthOfLongestSubstring("abcd")
    print(r)
    assert r == 4

    r = s.lengthOfLongestSubstring("abba")
    print(r)
    assert r == 2
