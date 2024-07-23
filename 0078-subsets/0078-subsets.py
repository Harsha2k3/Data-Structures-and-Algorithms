class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Take or not take pattern

        res = []

        def rec(i , subset):

            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            rec(i + 1 , subset)
            subset.pop()
            rec(i + 1 , subset)

        rec(0 , [])

        return res