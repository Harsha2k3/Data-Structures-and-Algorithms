class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # Similar to 40. Combination Sum II
        
        res = []

        def rec(ind , arr , subset):

            res.append(subset.copy())

            for i in range(ind , len(arr)):

                if i > ind and arr[i] == arr[i - 1]:
                    continue
                
                else:
                    subset.append(arr[i])
                    rec(i + 1 , arr , subset)
                    subset.pop()
        
        nums.sort()
        rec(0 , nums , [])

        return res
            

        


















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