def removeDuplicates(self, nums):
        #using to our advantage that it is an ordered list
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index+=1
        return index