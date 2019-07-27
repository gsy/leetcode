# -*- coding: utf-8 -*-


class Solution:
    def simplify(self, email):
        name, host = email.split('@')
        real_name = ''
        for char in name:
            if char == '+':
                break
            elif char == '.':
                continue
            else:
                real_name = real_name + char
        return real_name + '@' + host

    def numUniqueEmails(self, emails):
        result = set()
        for email in emails:
            email = self.simplify(email)
            result.add(email)
        return len(result)


if __name__ == '__main__':
    s = Solution()
    r = s.numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])
    assert r == 2
