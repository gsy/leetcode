# -*- coding: utf-8 -*-

class Solution:
    def duplicateZeros(self, arr):
        insert_flag = True
        for index, item in enumerate(arr):
            if item == 0:
                if insert_flag is True:
                    arr.insert(index, 0)
                    arr.pop(-1)
                    insert_flag = False
                else:
                    insert_flag = True
        print(arr)
        print('-'*30)

if __name__ == "__main__":
    s = Solution()
    s.duplicateZeros([])

    s = Solution()
    s.duplicateZeros([1, 2, 3])

    s = Solution()
    s.duplicateZeros([1, 2, 3, 0])

    s = Solution()
    s.duplicateZeros([0, 1, 2, 3])

    s = Solution()
    s.duplicateZeros([0, 1, 2, 3, 0])
