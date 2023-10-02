class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = 0
        l = []
        k = 1

        for i in range(len(nums)):
            l.append(nums[i]-1)
        
        for i in range(len(l)):
            for j in range(k,len(l)):
                res = max(res,l[i]*l[j])
            k += 1

        return res