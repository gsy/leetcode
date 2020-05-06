# 段落内有序，所以在一个段落内是可以使用二分搜索的
# 怎样确定一个段落？从 left 往后找，知道第一个比 left 小的 item 为止，都是一个段落
# 一个段落一个段落搜索


class Solution:
    def calculateRight(self, arr, length, left):
        # 递增的尽头，需要的包含的关系
        j = left + 1
        if j >= length:
            return length - 1

        if arr[j] > arr[left]:
            while j < length and arr[j] > arr[j-1]:
                j = j + 1
            return j - 1
        else:
            return left

    def search(self, arr, target):
        length = len(arr)
        left = 0
        while left < length:
            right = self.calculateRight(arr, length, left)

            # binary search
            current_left, current_right = left, right
            found = False
            # print("left:", current_left, "right:", current_right)

            while current_left <= current_right:
                mid = (current_left + current_right) // 2
                if arr[mid] == target:
                    found = True
                    current_right = mid
                    if current_left == current_right:
                        break
                elif arr[mid] > target:
                    current_right = mid - 1
                else:
                    current_left = mid + 1

            if found:
                return True
            else:
                left = right + 1

        return False
