class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def quicksort(self, nums, start, end):
        # sort in place
        length = end - start
        if length <= 1:
            return

        elif length == 2:
            if nums[start] > nums[start+1]:
                nums[start], nums[start+1] = nums[start+1], nums[start]
            return
        else:
            x = nums[start]
            i, j = start + 1, end - 1
            while i < j:
                while nums[i] <= x and i + 1 < end:
                    i = i + 1
                while nums[j] > x and j > start:
                    j = j - 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]

            nums[start], nums[j] = nums[j], nums[start]
            self.quicksort(nums, start, j)
            self.quicksort(nums, j+1, end)


    def wiggleSort(self, nums):
        # write your code here
        self.quicksort(nums, 0, len(nums))
        print "sorted:", nums
        for i in range(len(nums)):
            if i % 2 == 1 and (i + 1) < len(nums):
                nums[i], nums[i+1]= nums[i+1], nums[i]



if __name__ == "__main__":
    s = Solution()
    nums = [4,1,4,3,4,3,3,2,0,2]
    s.wiggleSort(nums)
    print "result:", nums
