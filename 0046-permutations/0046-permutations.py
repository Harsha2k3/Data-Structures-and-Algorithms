class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Using swapping

        # T.C = n! x n  (Combinations ==> n! and for loop ==> n)
        # S.C = O(n) auxiliary S.C for recursion

        # res = []

        # def rec(ind , nums):

        #     if ind == len(nums):
        #         res.append(nums.copy())
        #         return


        #     for i in range(ind , len(nums)):
        #         nums[ind] , nums[i] = nums[i] , nums[ind]
        #         rec(ind + 1 , nums)
        #         nums[ind] , nums[i] = nums[i] , nums[ind]
            
        # rec(0 , nums)

        # return res


        # # Takes extra memory for hashmap array
        # # T.C = n! x n  (Combinations ==> n! and for loop ==> n)
        # # S.C = O(n) normal S.C and O(n) auxiliary S.C for recursion
        
        res = []

        def rec(l , h):

            nonlocal res

            if len(l) == len(nums):
                res.append(l.copy())
                return

            for i in range(len(h)):
                if not h[i]:
                    l.append(nums[i])
                    h[i] = 1
                    rec(l , h)
                    l.pop()
                    h[i] = 0
        
        rec([] , [0] * len(nums))
        
        return res