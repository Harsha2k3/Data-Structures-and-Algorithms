from collections import deque 

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        q = deque()

        for i in nums:
            if i % 2 == 0:
                q.appendleft(i)
            else: 
                q.append(i)
                
        return list(q)