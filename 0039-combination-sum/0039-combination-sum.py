class Solution:
    def combinationSum(self, nums: List[int], t: int) -> List[List[int]]:

        res = []

        def rec(i , s , l):

            if i == len(nums):
                if s == 0:
                    res.append(l.copy())
                    return
            
            else:
                if nums[i] <= s:
                    l.append(nums[i])
                    rec(i , s - nums[i] , l)
                    l.pop()
                rec(i + 1 , s , l)

        rec(0 , t , [])

        return res