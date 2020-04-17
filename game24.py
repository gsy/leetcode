# -*- coding: utf-8 -*-


class Solution:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def times(self, a, b):
        return a * b

    def divide(self, a, b):
        return (1.0) * a / b

    def operators(self):
        for operator in (self.divide, self.times, self.add, self.minus):
            yield operator

    def safe_operate(self, operator, a, b):
        try:
            return operator(a, b)
        except Exception:
            return None

    def permutation(self, nums):
        if len(nums) <= 1:
            return [nums]
        elif len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]

        result = []
        for i in range(len(nums)):
            sub = [nums[j] for j in range(len(nums)) if j != i]
            for sub_per in self.permutation(sub):
                result.append([nums[i]] + sub_per)

        return result

    def get_two_out_of(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    for rest in self.permutation([nums[x] for x in range(len(nums)) if x not in (i, j)]):
                        yield [nums[i], nums[j]], rest

    def judgePoint24(self, nums):
        for (a, b), rest1 in self.get_two_out_of(nums):
            for operator in self.operators():
                tmp1 = self.safe_operate(operator, a, b)
                if tmp1 is None:
                    continue
                for (c, d), rest2 in self.get_two_out_of([tmp1] + rest1):
                    for operator in self.operators():
                        tmp2 = self.safe_operate(operator, c, d)
                        nums = [tmp2] + rest2
                        if tmp2 is None:
                            continue
                        for (e, f), rest3 in self.get_two_out_of(nums):
                            for operator in self.operators():
                                tmp3 = self.safe_operate(operator, e, f)
                                if tmp3 is None:
                                    continue
                                elif abs(tmp3 - 24) <= 0.0001:
                                    return True

        return False
