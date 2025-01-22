class Solution:
    def combinationSum2(self, nums: List[int], t: int) -> List[List[int]]:

        # Use this pattern when,
        # We are allowed to pick each number in input array only once
        # Input array has duplicates 
        # When we want the solution set to not have any duplicate combinations

        # Here if we use previous methods, we can't find duplicates in input array and we will use the same element present at different index and it leads to duplicates in solution set
        # So we use for loop here to find the duplicates in input array , so that solution set will not have any duplicate combinations

        res = []

        def rec(ind , t , l):

            nonlocal res

            if t == 0:
                res.append(l.copy())
                return
                
            if ind == len(nums):
                return

            for i in range(ind , len(nums)):
                
                if t < nums[i]:
                    break
                
                if i > ind and nums[i] == nums[i - 1]:
                    continue
                
                l.append(nums[i])
                rec(i + 1 , t - nums[i] , l)
                l.pop()
        
        nums.sort()
        rec(0 , t , [])

        return res
        

        # Note:-  (V.V.V.IMPORTANT)

        # [1,2,3,4,5,6]

        # sub-array ==> [3,4,5]  (Continuous)
        # Sub-sequence(sub-sets) ==> [2,4,5] (Might not be continuous, but follows order)
        # Combination  ==> [3,1,2] (Need not to follow the order too)






        # res = []

        # def rec(i , s , l):

        #     if(i == len(nums)):
        #         if(s == 0):
        #             res.append(sorted(l.copy()))
        #             return

        #     else:
        #         if(nums[i] <= s):
        #             l.append(nums[i])
        #             rec(i + 1 , s - nums[i] , l)
        #             l.pop()
        #         rec(i + 1 , s , l)

        # rec(0 , t , [])

        # res = set(tuple(sublist) for sublist in res) # Convert inner lists to tuples
        # res = [list(sublist) for sublist in res] # Convert tuples back to lists

        # return res