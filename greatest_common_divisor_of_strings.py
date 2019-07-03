# -*- coding: utf-8 -*-


class Solution:
    def can_divide(self, string, pattern):
        len_string = len(string)
        len_pattern = len(pattern)
        if len_string < len_pattern:
            return False
        elif len_string == len_pattern:
            return string == pattern
        elif len_string % len_pattern != 0:
            return False
        else:
            for i in range(0, len_string - len_pattern, len_pattern):
                substring = string[i: i + len_pattern]
                if substring != pattern:
                    return False
        return True

    def gcd_of_string(self, str2, length):
        if length == 0:
            return ""
        if length % 2 == 1:
            return [str2]
        else:
            left = str2[0:length/2]
            right = str2[length/2:]
            if left == right:
                return [str2, left] + self.gcd_of_string(left, length/2)
            else:
                return [str2]

    def gcdOfStrings(self, str1, str2):
        len_str2 = len(str2)
        if len_str2 == 0:
            return ""

        gcds = self.gcd_of_string(str2, len_str2)
        gcds = set(gcds)
        # print("gcds", gcds)

        for gcd in gcds:
            # can_divide = self.can_divide(str1, gcd)
            # print(str1, gcd, can_divide)
            if self.can_divide(str1, gcd):
                return gcd
        return ""
