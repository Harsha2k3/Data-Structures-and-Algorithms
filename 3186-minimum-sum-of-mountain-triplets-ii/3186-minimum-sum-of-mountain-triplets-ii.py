class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        left_min = [float("inf")]*n
        right_min = [float("inf")]*n
        
        min_sum = float("inf")
        
        for i in range(1,n):
            left_min[i] = min(left_min[i-1],nums[i-1])
            
        for i in range(n-2,-1,-1):
            right_min[i] = min(right_min[i+1],nums[i+1])
            if(left_min[i] < nums[i] and right_min[i] < nums[i]):
                min_sum = min(min_sum , left_min[i] + nums[i] + right_min[i])
                
        if(min_sum != float("inf")):
            return min_sum
        else:
            return -1