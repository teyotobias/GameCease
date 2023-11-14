
def jump(self, nums):
        if len(nums) <= 1: return 0
        jumps = 1
        left, right = 0, nums[0]
        while right < len(nums) - 1:
            jumps +=1
            nxt = max(nums[i] for i in range(left, right+1))
            left = right #most interesting part
            right += nxt
        return jumps