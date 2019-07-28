# -*- coding: utf-8 -*-

class Solution:
    def search_higher_temperature(self, current, mapping):
        for t in range(current+1, 101):
            if t in mapping:
                return mapping[t]
        return None

    def dailyTemperatures(self, ls):
        length = len(ls)
        result, temperature_to_index = [], {}
        for j in range(length-1, -1, -1):
            current = ls[j]
            higher = self.search_higher_temperature(current, temperature_to_index)
            temperature_to_index[current] = j
            for key, value in temperature_to_index.items():
                if key < current:
                    temperature_to_index[key] = j

            if higher:
                result.append(higher - j)
            else:
                result.append(0)
        return result[::-1]

if __name__ == "__main__":
    s = Solution()
    r = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(r)
    assert r == [1, 1, 4, 2, 1, 1, 0, 0]
