# -*- coding: utf-8 -*-


class Solution:
    def hashing(self, string):
        count = {}
        for char in string:
            count[char] = count.get(char, 0) + 1
        result = ''
        for index in range(ord('a'), ord('z')+1):
            key = chr(index)
            if key in count:
                result = result + key + str(count[key])
        return result

    def groupAnagrams(self, strs):
        slots = {}
        for string in strs:
            key = self.hashing(string)
            slots[key] = slots.get(key, []) + [string]

        return list(slots.values())


if __name__ == '__main__':
    s = Solution()
    r = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(r)
