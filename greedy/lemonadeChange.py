class Solution:
    def isValid(self, bill, cash):
        if bill == 5:
            return True
        else:
            need = bill - 5
            items = sorted(cash.items(), key=lambda item: item[0], reverse=True)
            values = [item[0] for item in items]

            for value in values:
                # 先换 n 张
                if need < 0:
                    return False

                if need == 0:
                    return True

                if need >= value and cash[value] > 0:
                    used = min(int(need / value), cash[value])
                    cash[value] = cash[value] - used
                    need = need - used * value

            return need == 0

    def lemonadeChange(self, bills):
        cash = {}
        for bill in bills:
            if self.isValid(bill, cash):
                cash[bill] = cash.get(bill, 0) + 1
            else:
                return False
        return True
