class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]

        # n + 1 是 [0 + n] + [1 + image(n)]
        pre = self.grayCode(n-1)
        # 怎么在前面补个1？
        length = len(pre)
        mask = 1 << (n-1)
        image = []
        for i in range(length):
            image.append(mask ^ pre[length - i - 1])
        return pre + image
