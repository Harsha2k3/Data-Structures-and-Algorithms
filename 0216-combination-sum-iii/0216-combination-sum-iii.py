class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [i for i in range(1 , 10)]

        res = []

        def rec(ind , l , s , nums):

            if len(l) == k and s == 0:
                res.append(l.copy())
                return

            for i in range(ind , len(nums)):
                l.append(nums[i])
                rec(i + 1 , l , s - nums[i] , nums)
                l.pop()

        rec(0 , [] , n , nums)

        return res