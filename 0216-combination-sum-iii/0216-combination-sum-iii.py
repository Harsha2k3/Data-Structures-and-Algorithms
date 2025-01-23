class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [i for i in range(1 , 10)]

        res = []

        def rec(ind , t , l):

            nonlocal res
            
            if t == 0 and len(l) == k:
                res.append(l.copy())
                return
                
            if ind == len(nums):
                return

            for i in range(ind , len(nums)):

                if t < nums[i]:
                    break

                l.append(nums[i])
                rec(i + 1 , t - nums[i] , l)
                l.pop()
        
        rec(0 , n , [])

        return res