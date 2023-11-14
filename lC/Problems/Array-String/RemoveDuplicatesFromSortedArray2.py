
def removeDuplicates(self, nums):
        n = len(nums)
        if(n <= 2):
            return n
        index = 2
        for i in range(2, n):
            if nums[i] != nums[index-2] :
                nums[index] = nums[i]
                index += 1
        return index