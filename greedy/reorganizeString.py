class Solution:
    def reorganizeString(self, S):
        chars = {}
        n = len(S)
        for c in S:
            chars[c] = chars.get(c, 0) + 1

        # key 要按照 value 排序
        items = sorted(chars.items(), key=lambda item: item[1], reverse=True)
        print(items)

        even, odd = 0, 1
        result = [""] * n
        for key, value in items:
            if value > (n + 1) // 2:
                return ""

            for i in range(value):
                if even < n:
                    result[even] = key
                    even = even + 2
                elif odd < n:
                    result[odd] = key
                    odd = odd + 2
                # print(result)

        return "".join(result)
