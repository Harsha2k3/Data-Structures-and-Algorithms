class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        
        bits = [0]*32
        
        for num in nums:
            for j in range(32):
                if((2 ** j) & num == 2 ** j):
                    bits[j] += 1
                    
        res = 0
        
        for i in range(32):
            if(bits[i] >= k):
                res += 2 ** i
                
        return res