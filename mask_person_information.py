# -*- coding: utf-8 -*-

import string


class Solution:
    def mask_email(self, email):
        name, host = email.split('@')
        mask_name = name[0].lower() + "*****" + name[-1].lower()
        domains = host.split('.')
        return mask_name + "@" + ".".join(domain.lower() for domain in domains)

    def mask_phone(self, phone):
        digits = []
        for char in phone:
            if char in string.digits:
                digits.append(char)

        length = len(digits)
        if length == 10:
            return "***-***-{}".format("".join(digits[-4:]))
        else:
            return "+{}-***-***-{}".format("*"*(length-10), "".join(digits[-4:]))

    def maskPII(self, string):
        if "@" in string:
            return self.mask_email(string)
        else:
            return self.mask_phone(string)


if __name__ == '__main__':
    s = Solution()
    r = s.maskPII("LeetCode@LeetCode.com")
    print(r)
    assert r == "l*****e@leetcode.com"

    r = s.maskPII("AB@qq.com")
    assert r == "a*****b@qq.com"

    r = s.maskPII("1(234)567-890")
    print(r)
    assert r == "***-***-7890"

    r = s.maskPII("86-(10)12345678")
    print(r)
    assert r == "+**-***-***-5678"
