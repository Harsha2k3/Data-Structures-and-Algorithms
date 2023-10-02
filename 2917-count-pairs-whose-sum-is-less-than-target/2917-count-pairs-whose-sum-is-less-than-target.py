class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        count = 0

        for i in range(len(nums)):
            k = i+1
            for j in range(k,len(nums)):
                if(nums[i]+nums[j] < target):
                    count += 1
        
        return count