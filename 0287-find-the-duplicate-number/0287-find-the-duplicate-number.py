class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        s = set()            # Empty set
    
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)        # Append i to set s