# -*- coding: utf-8 -*-


class Solution:
    def compress(self, chars):
        length = len(chars)
        if length <= 1:
            return length

        processed = 1
        prev = chars[0]
        index = 1
        count = 1

        while processed < length:
            char = chars[index]
            if char == prev:
                count = count + 1
                if count == 2:
                    chars[index] = str(count)
                    index = index + 1
                else:
                    tmp = count
                    carry = count in (10, 100, 1000, 10000)  # 位数变多
                    if carry:
                        i = index
                    else:
                        i = index - 1
                    while tmp != 0:
                        chars[i] = str(tmp % 10)
                        i = i - 1
                        tmp = tmp / 10
                    if carry:   # 位数变多
                        index = index + 1
                    else:
                        chars.pop(index)
            else:
                count = 1
                index = index + 1
            processed = processed + 1
            prev = char

        print(chars)
        return len(chars)
