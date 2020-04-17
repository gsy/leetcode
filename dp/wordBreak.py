class Solution:
    def wordBreak(self, s, wordDict):
        length = len(s)
        A = [False] * length
        breakpoints = {}

        for i in range(length):
            flag = False
            for j in range(i+1):
                word = s[j:i+1]
                if word in wordDict:
                    if j == 0 or A[j-1]:
                        flag = True
                        if j in breakpoints:
                            ls = breakpoints[j]
                            ls.append((j, i))
                        else:
                            ls = [(j, i)]
                            breakpoints[j] = ls

            A[i] = flag

        # 深度优先遍历
        result = []
        seen = []
        next_id = 0
        while True:
            ls = breakpoints[next_id]
            for bp in ls:
                candidate = bp[1] + 1
                if candidate not in seen:
                    next_id = candidate


        return breakpoints
