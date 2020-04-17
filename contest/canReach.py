class Solution:
    def canReach(self, arr, start):
        # 构建 DAG, 使用广度优先搜索

        mapping = {}
        length = len(arr)
        for i, step in enumerate(arr):
            ls = []
            if (i + step) >= 0 and (i + step) < length:
                ls.append(i+step)
            if (i - step) >= 0 and (i - step) < length:
                ls.append(i-step)
            mapping[i] = ls

        stack = mapping[start]
        seen = []
        while stack:
            # 广度优先怎么写？
            current = stack.pop(0)
            if arr[current] == 0:
                return True

            next_level = mapping[current]
            seen.append(current)
            tmp = []
            for item in next_level:
                if item not in seen:
                    tmp.append(item)

            stack = stack + tmp

        return False
