class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # Similar to 40. Combination Sum II
        # 40. Combination Sum II pattern, but we have to add every combination to the res

        res = []

        def rec(ind , l):

            nonlocal res

            res.append(l.copy())

            for i in range(ind , len(nums)):

                if i > ind and nums[i] == nums[i - 1]:
                    continue
                
                l.append(nums[i])
                rec(i + 1 , l)
                l.pop()
        
        nums.sort()
        rec(0 , [])

        return res


        # (Or)


        # # Brute force
        # # T.C = m x log m (set ==> log m)  , where m = 2 ^ n
        # # We will remove this logarithmic factor by optimized approach

        # res = []

        # def rec(i , subset):

        #     if i >= len(nums):
        #         res.append(sorted(subset.copy()))
        #         return

        #     subset.append(nums[i])
        #     rec(i + 1 , subset)
        #     subset.pop()
        #     rec(i + 1 , subset)

        # rec(0 , [])

        # # Sorting
        # res = set(tuple(sublist) for sublist in res) # Convert inner lists to tuples
        # res = [list(sublist) for sublist in res] # Convert tuples back to lists

        # return res