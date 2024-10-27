class Solution:
    def combinationSum(self, nums: List[int], t: int) -> List[List[int]]:

        # Some what like take or not take pattern
        # Use this pattern when,
        # We are allowed to pick each number in input array more than once

        res = []

        def rec(i , l , t):

            nonlocal res

            if i == len(nums):
                if t == 0:
                    res.append(l.copy())
                return        

            if nums[i] <= t:
                l.append(nums[i])
                rec(i , l , t - nums[i])
                l.pop()
            rec(i + 1 , l , t)
        
        rec(0 , [] , t)

        return res