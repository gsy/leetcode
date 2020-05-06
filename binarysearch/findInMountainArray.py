# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def get(self, A, index, length):
        if index < 0 or index >= length:
            return None

        return A.get(index)

    def getLength(self, A):
        return A.length()

    def get2(self, A, index, length):
        if index < 0 or index >= length:
            return None

        return A[index]

    def getLength2(self, A):
        return len(A)

    def findInMountainArray(self, target, mountain_arr):
        # 只有一个峰值
        # 值可以重复
        # 找到 index 最小的值
        length = self.getLength2(mountain_arr)
        candidates = [(0, length-1)]
        result = length + 1
        up_left, up_right = 0, length - 1
        down_left, down_right = 0, length - 1

        while len(candidates) > 0:
            # print("candidates", candidates)
            left, right = candidates.pop(0)
            print("left", left, "right", right)
            found, tmp = False, None

            while left <= right:
                if (right - left) <= 1:
                    for i in range(left, right+1):
                        value = self.get2(mountain_arr, i, length)
                        if value == target:
                            found = True
                            tmp = i
                    break

                mid = (left + right) // 2
                before, after = mid - 1, mid + 1

                value_mid = self.get2(mountain_arr, mid, length)
                value_before = self.get2(mountain_arr, before, length)
                value_after = self.get2(mountain_arr, after, length)

                if (value_before is not None and value_mid > value_before) and (value_after is not None and value_mid > value_after):
                    # peek
                    up_right = min(up_right, mid)
                    down_left = max(down_left, mid)
                    if value_mid > target:
                        candidates.append((up_left, mid-1))
                        candidates.append((mid+1, down_right))
                        break

                    elif value_mid == target:
                        found = True
                        tmp = mid
                        break
                    else:
                        break

                elif (value_before is not None and value_mid > value_before) and (value_after is not None and value_mid < value_after):
                    # trend = "up"
                    if value_mid == target:
                        found = True
                        tmp = mid
                        break
                    elif value_mid > target:
                        candidates.append((up_left, mid-1))
                        candidates.append((max(mid+1, down_left), down_right))
                        break
                    else:
                        left = mid + 1
                        up_left = max(up_left, left)

                elif (value_before is not None and value_mid < value_before) and (value_after is not None and value_mid > value_after):
                    # trend = "down"
                    if value_mid == target:
                        found = True
                        tmp = mid
                        candidates.append((up_left, min(mid-1, up_right)))
                        break
                    elif value_mid > target:
                        candidates.append((mid+1, down_right))
                        candidates.append((up_left, min(mid-1, up_right)))
                        break
                    else:
                        right = mid - 1
                        down_right = min(right, down_right)

            if found and tmp < result:
                result = tmp

        return -1 if result == length + 1 else result
