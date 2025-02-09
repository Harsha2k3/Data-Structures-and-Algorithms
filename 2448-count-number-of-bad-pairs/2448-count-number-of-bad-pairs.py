from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        # Once you rearrange the equation j - i != nums[j] - nums[i] 
        # it becomes j - nums[j] != i - nums[i]. Now you can substract 
        # every element with index. The problem becomes 
        # how many different elements are there for each element 
        # to its left  
        
        # i - nums[i] = [4 , 0 , 1 , 0]

        for i in range(len(nums)):
            nums[i] = i - nums[i]

        cnt = defaultdict(int)
        res = 0

        for i in range(len(nums)):
            res += i - cnt[nums[i]]
            cnt[nums[i]] += 1

        return res