import math

class Solution:
    def arraySign(self, nums: List[int]) -> int:

        p = math.prod(nums)

        if(p>0):
            return 1
        elif(p<0):
            return -1
        else:
            return 0