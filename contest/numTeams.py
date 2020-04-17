# 最长的升降序系列
class Solution:
    def numTeams(self, rating):
        length = len(rating)
        if length < 3:
            return 0

        result = [[0] * length] * 2
        for i in range(1, length):
            for j in range(i-1):
                if rating[j] > rating[i]:
                    result[0][i] = result[0][j] + 1  # 0 降序
                elif rating[j] < rating[i]:
                    result[1][i] = result[1][j] + 1  # 1 升序

        print(result)
        # return sum(result[0][2:]) + sum(result[1][2:])
        return 0


if __name__ == '__main__':
    s = Solution()
    r = s.numTeams([2, 5, 4, 3, 1])
    print(r)

    r = s.numTeams([2, 1, 3])
    print(r)

    r = s.numTeams([1, 2, 3, 4])
    print(r)
