
def productExceptSelf(self, nums):
        #for i in range(x,y,z) - start,stop,step
        #using division property
        # product = 1
        # num_zeros = 0
        # n = len(nums)
        # for i in range(n):
            # if nums[i] == 0:
                # num_zeros += 1
            # else:
                # product *= nums[i]
        # if num_zeros > 1:
            # return [0 for num in nums]
        # if num_zeros != 0:
            # return [0 if num == 0 else int(product) for num in nums]
        # return [int(product/num) for num in nums]
    
        #without using division property
        #easy solution: get products of everything before and after each value
        prefix_product = 1
        postfix_product = 1
        n = len(nums)
        results = [0]*n
        for i in range(n):
            results[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1, -1, -1): #n-1 because start includes index indicated
        #-1 as the stop because stop does not include index indicated-stops at 0
            results[i] *= postfix_product
            postfix_product *= nums[i]
        return results