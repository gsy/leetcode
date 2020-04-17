class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        result = 0
        for value1 in arr1:
            flag = True
            for value2 in arr2:
                if abs(value1 - value2) <= d:
                    flag = False
            if flag:
                result = result + 1

        return result
