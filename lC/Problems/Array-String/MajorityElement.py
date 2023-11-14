
def majorityElement(self, nums):
        n = len(nums)
        nums.sort()
        return nums[n//2]