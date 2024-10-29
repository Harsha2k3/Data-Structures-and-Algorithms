class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0

        def rec(i , xor):

            nonlocal res

            if i == len(nums):
                res += xor
                return

            # l.append(nums[i])
            xor ^= nums[i]
            rec(i + 1 , xor)
            # l.pop()
            xor ^= nums[i]
            rec(i + 1 , xor)
        
        rec(0 , 0)
        
        return res