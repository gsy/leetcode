# 段落内有序，所以在一个段落内是可以使用二分搜索的
# 怎样确定一个段落？从 left 往后找，知道第一个比 left 小的 item 为止，都是一个段落
# 一个段落一个段落搜索


class Solution:
    def search(self, arr, target):
        length = len(arr)
        left = 0
        while left < length:
            # get right

            if left == right:
                if arr[left] == target:
                    return left
                else:
                    continue

            # binary search
            current_left, current_right = left, right
            found = False
            print("left:", current_left, "right:", current_right)
            result = None
            while current_left <= current_right:
                mid = (current_left + current_right) // 2
                if arr[mid] == target:
                    print(f"mid: {arr[mid]}({mid})")
                    found = True
                    current_right = mid
                    result = mid
                    if current_left == current_right:
                        break
                elif arr[mid] > target:
                    current_right = mid - 1
                else:
                    current_left = mid + 1

            if found:
                return result
            else:
                left = right + 1

        return -1
