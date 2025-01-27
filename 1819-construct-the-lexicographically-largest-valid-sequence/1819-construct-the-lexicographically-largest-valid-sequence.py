class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        # Length of the answer = n + (n - 1)

        res = [0] * ((2 * n) - 1)

        nums = [i for i in range(1 , n + 1)]

        nums.reverse()

        # res[0] = nums[0]
        # res[nums[0]] = nums[0]

        fres = []

        def rec(ind , h , res):

            nonlocal fres

            if fres:
                return

            if ind == len(res):
                fres = res.copy()
                return

            # Skip already filled positions
            if res[ind] :  
                rec(ind + 1 , h , res)
            else:
                for i in range(len(h)):
                    if not h[i]:
                        if nums[i] == 1:
                            res[ind] = nums[i]
                            h[i] = 1
                            rec(ind + 1 , h , res)
                            res[ind] = 0
                            h[i] = 0

                        if ind + nums[i] <= len(res) - 1 and not res[ind + nums[i]]:
                            res[ind] = nums[i]
                            res[ind + nums[i]] = nums[i]
                            h[i] = 1
                            rec(ind + 1 , h , res)
                            res[ind] = 0
                            res[ind + nums[i]] = 0
                            h[i] = 0
        
        rec(0 , [0] * n , res)

        return fres