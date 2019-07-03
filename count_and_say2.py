# -*- coding: utf-8 -*-


class Solution:
    def do_count_and_say(self, string):
        prev = None
        count = 0
        result = ""
        for char in string:
            if not prev:
                prev = char
                count = 1
            elif prev == char:
                count = count + 1
            else:
                # say & reset
                result = result + str(count) + prev
                count = 1
            prev = char
        result = result + str(count) + char
        return result

    def countAndSay(self, n):
        # 相同的字符计数
        if n == 0:
            return ""

        result = "1"
        for i in range(n-1):
            result = self.do_count_and_say(result)
        return result
