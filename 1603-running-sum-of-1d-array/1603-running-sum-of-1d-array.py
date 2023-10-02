class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        j = -2
        k = -1
        l = []
        
        for i in nums:
            l.append(i)

        l[-1] = sum(nums)

        for i in range(len(nums)-1):
            l[j] = l[k] - nums[k]
            j -= 1
            k -= 1
        
        return l