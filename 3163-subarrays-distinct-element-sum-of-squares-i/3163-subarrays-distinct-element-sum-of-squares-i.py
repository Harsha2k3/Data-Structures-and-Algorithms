class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        res = 0
        n = len(nums)
        
        for i in range(n):
            distinct = set()
            for j in range(i,n):
                distinct.add(nums[j])
                res += len(distinct) ** 2
                
        return res