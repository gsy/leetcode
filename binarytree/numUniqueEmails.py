class Solution:
    def convert(self, email):
        localname, domain = email.split("@")
        name = ""
        for char in localname:
            if char == '.':
                continue
            elif char == '+':
                break
            else:
                name = name + char
        return name + "@" + domain

    def numUniqueEmails(self, emails):
        result = set()
        for email in emails:
            address = self.convert(email)
            print(address)
            result.add(address)
        return len(result)
