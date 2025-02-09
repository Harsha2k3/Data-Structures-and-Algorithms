from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j]) 

        # [18 , 0 , 0 , 18]

        for i in range(len(nums)):

            nums[i] = nums[i] - int(str(nums[i])[::-1])

        count = defaultdict(int)
        res = 0

        for i in range(len(nums)):
            res += count[nums[i]]
            count[nums[i]] += 1
        
        return res % ((10 ** 9) + 7)