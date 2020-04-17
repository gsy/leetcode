# -*- coding: utf-8 -*-

class Solution:
    def build_mapping(self, arr2):
        return {value: index for index,value in enumerate(arr2)}

    def weight(self, item):
        return self.mapping.get(item, self.maximum+item)


    def relativeSortArray(self, arr1, arr2):
        self.maximum = len(arr2)
        self.mapping = self.build_mapping(arr2)
        return sorted(arr1, key=self.weight)

if __name__ == "__main__":
    s = Solution()
    r = s.relativeSortArray(arr1=[2,3,1,3,2,4,6,7,9,2,19], arr2=[2,1,4,3,9,6])
    assert r == [2,2,2,1,4,3,3,9,6,7,19]

    r = s.relativeSortArray(arr1=[28,6,22,8,44,17], arr2=[22,28,8,6])
    assert r == [22,28,8,6,17,44]
