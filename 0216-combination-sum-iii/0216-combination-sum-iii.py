class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [i for i in range(1 , 10)]
        res = []

        def rec(l , ind , t):

            if len(l) == k and t == 0:
                res.append(l.copy())
                return

            for i in range(ind , len(nums)):
                l.append(nums[i])
                rec(l , i + 1 , t - nums[i])
                l.pop()
        
        rec([] , 0 , n)

        return res