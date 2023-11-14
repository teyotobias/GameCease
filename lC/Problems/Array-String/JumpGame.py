
def canJump(self, nums):
        n = len(nums)
        last_index = n - 1
        #start, stop, step
        for i in range(n-2, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        return last_index == 0