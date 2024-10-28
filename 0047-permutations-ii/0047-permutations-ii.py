class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []

        def rec(ind, nums):

            if ind == len(nums):
                res.append(nums.copy())
                return

            seen = set()
            for i in range(ind, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                
                nums[ind], nums[i] = nums[i], nums[ind]
                rec(ind + 1, nums)
                nums[ind], nums[i] = nums[i], nums[ind]

        rec(0, nums)

        return res



        # # T.C = n! x n  (Combinations ==> n! and for loop ==> n)
        # # S.C = O(n) auxiliary S.C for recursion

        # res = []

        # def rec(ind , nums):

        #     if ind > len(nums) - 1:
        #         res.append(nums.copy())
        #         return

        #     for i in range(ind , len(nums)):
        #         if i > ind and nums[i] == nums[i - 1]:
        #             continue
                
        #         nums[ind] , nums[i] = nums[i] , nums[ind]
        #         rec(ind + 1 , nums)
        #         nums[ind] , nums[i] = nums[i] , nums[ind]

        # nums.sort()
        # rec(0 , nums)

        # res_final = set()

        # for i in res:
        #     res_final.add(tuple(i))

        # return list(res_final)