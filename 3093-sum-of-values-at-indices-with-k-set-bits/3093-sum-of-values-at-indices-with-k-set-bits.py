class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        res = 0

        for i in range(len(nums)):
            j = i
            count = 0
            while(i != 0):
                if(i & 1 == 1):
                    count += 1
                i = i >> 1
            if(count == k):
                res += nums[j]

        return res