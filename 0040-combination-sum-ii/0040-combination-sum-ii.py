class Solution:
    def combinationSum2(self, nums: List[int], t: int) -> List[List[int]]:

        res = []

        def rec(ind , arr , t , l):

            if(t == 0):
                res.append(l.copy())
                return

            for i in range(ind , len(arr)):

                if(i > ind and arr[i] == arr[i - 1]):
                    continue
                
                if(arr[i] > t):
                    break

                else:
                    l.append(arr[i])
                    rec(i + 1 , arr , t - arr[i] , l)
                    l.pop()

        nums.sort()
        rec(0 , nums , t , [])

        return res


        # Note:-

        # [1,2,3,4,5,6]

        # sub-array ==> [3,4,5]  (Continuous)
        # Sub-sequence ==> [2,4,5] (Might not be continuous, but follows order)
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