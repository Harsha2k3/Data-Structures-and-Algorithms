class Solution:
    def pivotArray(self, nums: List[int], p: int) -> List[int]:

        l = []

        for i in nums:
            if(i < p):
                l.append(i)

        for i in nums:
            if(i == p):
                l.append(i)

        for i in nums:
            if(i > p):
                l.append(i)
        
        return l