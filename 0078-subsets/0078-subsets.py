class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res_final = []

        for i in range(2**n):
            res = []
            for j in range(n):
                if(((1 << j) & i) != 0):
                    res.append(nums[j])
            res_final.append(res)

        return res_final