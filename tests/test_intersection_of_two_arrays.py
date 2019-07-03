# -*- coding: utf-8 -*-

from intersection_of_two_arrays import Solution

if __name__ == '__main__':
    s = Solution()
    r = s.intersect([1,2,2,1], [2,2])
    print(r)

    r = s.intersect([4, 9, 5], [9,4,9,8,4])
    print(r)

    r = s.intersect([1,2,2,1], [2, 1])
    print(r)
