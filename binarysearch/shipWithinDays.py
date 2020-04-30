# 1. 大于1天的
# 2. 接近平均的，可能比平均大，因为要按照顺序
# 3. 在这个范围内猜？


class Solution:
    def withInDays(self, weights, capacity, days):
        current = 0
        needs = 0
        for i, weight in enumerate(weights):
            current = current + weight
            if current > capacity:
                needs = needs + 1
                current = weight
            elif current == capacity:
                needs = needs + 1
                current = 0

            if needs > days:
                return 1

        if current > 0:
            needs = needs + 1

        if needs > days:
            return 1
        elif needs == days:
            return 0
        return -1

    def shipWithinDays(self, weights, D):
        total, heaviest, length = 0, None, 0
        for weight in weights:
            total = total + weight
            length = length + 1
            if heaviest is None:
                heaviest = weight
            elif weight > heaviest:
                heaviest = weight
        avg = total // length

        left = max(avg, heaviest)
        right = total

        # 在 left, right 之间猜
        while left < right:
            mid = (left + right) // 2

            result = self.withInDays(weights, mid, D)
            # 需要的天数比 D 多
            if result > 0:
                left = mid + 1
            else:
                right = mid

        return right
