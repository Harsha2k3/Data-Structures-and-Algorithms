class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d={}
        m=-1
        for i in range(len(nums)):
            sumdigit=0
            for j in str(nums[i]):
                sumdigit+=int(j)
            if sumdigit not in d:
                d[sumdigit]=nums[i]
            else:
                m=max(d[sumdigit]+nums[i],m)
                d[sumdigit]=max(d[sumdigit],nums[i])
        return m