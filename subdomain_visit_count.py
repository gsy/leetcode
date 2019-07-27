# -*- coding: utf-8 -*-

class Solution:
    def parent_domain(self, domain):
        if '.' not in domain:
            return []

        domains = domain.split('.')
        result = []
        for i in range(1, len(domains)):
            result.append(".".join(domains[i:]))
        return result

    def subdomainVisits(self, cpdomains):
        count = {}
        for item in cpdomains:
            item = item.split(" ")
            visits = int(item[0])
            domain = item[1]
            count[domain] = count.get(domain, 0) + visits
            for d in self.parent_domain(domain):
                count[d] = count.get(d, 0) + visits

        result = []
        for key, value in count.items():
            result.append("{} {}".format(value, key))
        return result

if __name__ == "__main__":
    s = Solution()
    r = s.subdomainVisits(["9001 discuss.leetcode.com"])
    print(r)
    assert r == ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]

    r = s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    print(r)
    assert len(r) == len(["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"])
