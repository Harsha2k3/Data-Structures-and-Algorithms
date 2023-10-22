class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        if(len(nums) < 3):
            return -1
        
        min_sum = float('inf')
        
        for i in range(1,len(nums)-1):
            left_min = min(nums[:i])              # Maximum element on right side 
            right_min = min(nums[i+1:])           # Maximum element on left side 
            
            if(nums[i] > left_min and nums[i] > right_min):
                min_sum = min(min_sum , left_min + nums[i] + right_min)
                
                
        if(min_sum != float("inf")):
            return min_sum
        else:
            return -1