class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        il = 1      # Increasing length
        dl = 1      # Decreasing length
        
        ml = 1      # Max length
        
        for i in range(1 , len(nums)):

            if nums[i] > nums[i - 1]:
                il += 1
                dl = 1

            elif nums[i] < nums[i - 1]:
                dl += 1
                il = 1

            else:
                il = 1
                dl = 1
            
            ml = max(ml , il , dl)
        
        return ml