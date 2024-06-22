class Solution(object):
    def minOperations(self, nums):
        
        flips = 0
        
        for i in range(len(nums)):
            if flips % 2 == 1:
                nums[i] = 1 - nums[i] 
            
            if nums[i] == 0:
                flips += 1
        
        return flips