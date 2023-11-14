
def rotate(self, nums, k):
        n = len(nums)
        if k > n:
            k = k % n
        
        self.reverseNums(nums, 0, (n-k)-1)
        self.reverseNums(nums, n - k, n - 1)
        self.reverseNums(nums, 0, n - 1)
        """
        Do not return anything, modify nums in-place instead.
        """
def reverseNums(self, nums, i, j):
    temp = 0
    while i < j:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i+=1
        j-=1