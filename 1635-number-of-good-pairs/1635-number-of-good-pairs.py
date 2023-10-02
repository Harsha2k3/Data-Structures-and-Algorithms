class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count = 0

        for i in range(len(nums)):
            if(nums[i] in nums[i+1:]):
                count += nums[i+1:].count(nums[i])
        
        return count