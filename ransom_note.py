# -*- coding: utf-8 -*-


class Solution:
    def charset(self, string):
        result = {}
        for char in string:
            result[char] = result.get(char, 0) + 1

        return result

    def canConstruct(self, ransomNote, magazine):
        charset_of_ransom = self.charset(ransomNote)
        charset_of_magazine = self.charset(magazine)

        for key, value in charset_of_ransom.items():
            if key not in charset_of_magazine:
                return False
            elif value > charset_of_magazine[key]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    r = s.canConstruct("aa", "ab")
    assert r is False
