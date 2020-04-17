class Solution:
    def backtrack(self, num):
        hours = [0, 1, 2, 4, 8]
        minutes = [0, 1, 2, 4, 8, 16, 32]

        result = []
        for hour in range(5):
            # 选一个灯
            if hour <= num:
                minute = num - hour
                if minute < len(minutes):
                    minutes = hours[hour] * 60 + minutes[minute]
                    result.append(minutes)
        return result

    def readBinaryWatch(self, num):
        result = []
        return result
