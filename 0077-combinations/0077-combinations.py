class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = [i for i in range(1 , n + 1)]

        res = []

        def rec(ind , l):

            nonlocal res

            if len(l) == k:
                res.append(l.copy())
                return

            for i in range(ind , len(nums)):
                l.append(nums[i])
                rec(i + 1 , l)
                l.pop()
        
        rec(0 , [])

        return res