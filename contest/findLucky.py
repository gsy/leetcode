class Solution:
    def findLucky(self, arr):
        count = {}
        for item in arr:
            count[item] = count.get(item, 0) + 1

        result = -1
        for key, value in count.items():
            if key == value:
                if result == -1:
                    result = key
                elif key > result:
                    result = key

        return result
