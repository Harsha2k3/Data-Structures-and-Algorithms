import math as m

class Solution:

    # We have to find no.of bananas per hour (k) that koko eats, so that it can complete all of the piles with in h hours
        # Say, [3,6,7,11] and h = 8
# K = 1 ==> hr's = [3hr's,6hr's,7hr's,11hr's] ==> sum > 8
# K = 2 ==> hr's = [2hr's,3hr's,4hr's,6hr's]  ==> sum > 8
# K = 3 ==> hr's = [1hr's,2hr's,3hr's,4hr's]  ==> sum > 8
# K = 4 ==> hr's = [1hr's,2hr's,2hr's,3hr's]  ==> sum = 8
# So, return 4
# k lies between 1 and max(piles array)

    def get_hrs(self,k,piles):

        th = 0            # Total hrs
        for i in piles:
            th += m.ceil(i/k)
        return th

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        res = float("inf")

        while(left <= right):


            mid = (left + right) // 2

            # if(self.get_hrs(mid,piles) == h):
            #     return mid

            if(self.get_hrs(mid,piles) > h):
                left = mid + 1
            
            else:
                res = min(res,mid)
                right = mid - 1

        return res