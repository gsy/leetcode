# -*- coding: utf-8 -*-


class Solution:
    def hashing(self, string):
        primes, result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103], 1
        for char in string:
            result = result * primes[ord(char) - ord('a')]
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
