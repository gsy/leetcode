# -*- coding: utf-8 -*-


class Solution:
    def get_digits(self, num):
        digits = []
        while num != 0:
            digits.append(num % 10)
            num = num / 10
        return digits

    def permutation(self, list_of_ls, current):

        for ls in list_of_ls:
            print(ls)
            for i in range(len(ls) + 1):
                result = ls[:i] + [current] + ls[i:]
                print(ls, i, result)
                yield result

    def reduce_permutation(self, ls):
        # ls 先排序

        list_of_ls = [[]]
        for item in ls:
            tmp = []
            for ls in self.permutation(list_of_ls, item):
                tmp.append(ls)
            list_of_ls = tmp

        return list_of_ls

    def nextGreaterElement(self, n):
        # 从个位开始算？
        digits = self.get_digits(n)
        numbers = self.reduce_permutation(digits)
        for number in numbers:
            if number > n:
                return number
        return -1


if __name__ == '__main__':
    s = Solution()
    # r = s.nextGreaterElement(12)
    # print(r)

    r = s.reduce_permutation([1, 2, 3])
    print('-' * 30)
    for x in r:
        print(x)
