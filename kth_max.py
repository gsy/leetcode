class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def buildKMaxTree(self, array, parent, length):
        left = parent * 2 + 1
        right = parent * 2 + 2
        if left < length:
            self.buildKMaxTree(array, left, length)
            if array[left] > array[parent]:
                array[left], array[parent] = array[parent], array[left]
        if right < length:
            self.buildKMaxTree(array, right, length)
            if array[right] > array[parent]:
                array[right], array[parent] = array[parent], array[right]


    def kthLargestElement(self, k, A):
        length = len(A)
        for i in range(k):
            self.buildKMaxTree(A, 0, length - i)
            # print "array:", A
            A[0], A[length-1-i] = A[length-1-i], A[0]

        if k <= len(A) and k >= 1:
            return A[length-k]



if __name__ == "__main__":
    s = Solution()
    k = 6
    array = [9,3,2,4,8]
    array2 = [1,2,3,4,5]
    kth = s.kthLargestElement(k, array2)
    print "{}th: {}".format(k, kth)
