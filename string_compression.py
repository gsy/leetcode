# -*- coding: utf-8 -*-


class Solution:
    def compress(self, chars):
        result = ""
        prev, count = None, 1
        for char in chars:
            if prev is None:
                prev = char
                continue

            if char == prev:
                count = count + 1
            else:
                if count > 1:
                    result = result + prev + str(count)
                else:
                    result = result + prev
                prev, count = None, 1

        print(result)
        return len(result)


if __name__ == '__main__':
    s = Solution()
    r = s.compress(["a","a","b","b","c","c","c"])
    print(r)



fridge-e625e17a2334,fridge-2ea1b1eea9c5,fridge-967cf4648e9e,fridge-2ea1b1eea9c5,fridge-b683f563f2d9,fridge-de19b1bd46fa,fridge-46013c04d7e6,fridge-46013c04d7e6,fridge-2226964824e8,fridge-7ad1d9c4951a,





fridge-7ad1d9c4951a,fridge-e6c70b5c9f08,fridge-9e9280046836,fridge-c2be39540068,fridge-ba65fa44ba00,fridge-1ef9f0034dee,fridge-92abd64fec32,fridge-728dca12ded4,fridge-c2be39540068,fridge-c2be39540068,



fridge-c2be39540068,fridge-46013c04d7e6,fridge-8a464a6e3312,fridge-f627a2661a4b,fridge-5a84f2bd2a62,



fridge-8a464a6e3312,fridge-f627a2661a4b,fridge-5a84f2bd2a62,fridge-f627a2661a4b,fridge-c2be39540068,fridge-7ad1d9c4951a,fridge-5a84f2bd2a62,fridge-7ad1d9c4951a,fridge-229e49c98dd2,fridge-3ea4245b03f6


fridge-3ea4245b03f6,fridge-1ef9f0034dee,fridge-be56ffbb85b1,fridge-1ef9f0034dee,fridge-e6c70b5c9f08,fridge-be56ffbb85b1,fridge-be56ffbb85b1,fridge-be56ffbb85b1,fridge-e6c70b5c9f08,fridge-ba65fa44ba00,


# 今天内所有超时的 device_id
select distinct device_id from orders where status = 10 and create_time >= 1563033600;
