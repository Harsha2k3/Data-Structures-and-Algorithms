class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:

        s = 0
        d = 0

        for i in range(len(nums)):
            if len(str(nums[i])) == 1:
                s += nums[i]
            if len(str(nums[i])) == 2:
                d += nums[i]

        if  s > sum(nums) - s or d > sum(nums) - d:
            return True 
        return False