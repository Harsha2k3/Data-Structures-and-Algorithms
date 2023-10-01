import numpy as np
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        if(k > len(nums)):
            k = k - len(nums)
        
        t = nums[0:len(nums)-k]

        nums[0:len(nums)-k] = nums[len(nums)-k:]
        nums[len(nums)-k:] = t

        return nums