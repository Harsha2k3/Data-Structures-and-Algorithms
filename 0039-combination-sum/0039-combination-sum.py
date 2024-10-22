class Solution:
    def combinationSum(self, nums: List[int], t: int) -> List[List[int]]:

        # Some what like take or not take pattern
        # Use this pattern when,
        # We are allowed to pick each number in input array more than once

        res = []

        def rec(i , t , l):

            if i == len(nums):
                if t == 0:
                    res.append(l.copy())
                    return

            else:
                if nums[i] <= t:
                    l.append(nums[i])
                    rec(i , t - nums[i] , l)
                    l.pop()
                rec(i + 1 , t , l)
        
        rec(0 , t , [])

        return res