class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Take or not take pattern

        res = []

        def rec(i , l):

            nonlocal res

            if i == len(nums):
                res.append(l.copy())
                return

            l.append(nums[i])
            rec(i + 1 , l)
            l.pop()
            rec(i + 1 , l)
        
        rec(0 , [])
        
        return res