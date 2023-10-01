class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        l = []
        count = 0

        for i in nums:
            if(i not in l):
                l.append(i)

        for i in range(len(l)):
            for j in range(len(nums)):
                if(l[i] == nums[j]):
                    count += 1
                    if(count >= n/2):
                        res = nums[j]
                        count = 0
                        break
        
        return res