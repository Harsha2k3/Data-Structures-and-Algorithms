# Fixed Sized Sliding Window

class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count = 0

        k = 3

        curr_arr = s[:k]

        if(len(set(curr_arr)) == 3):
                count += 1

        for i in range(1,len(s)-k+1):
            curr_arr = s[i:k+i]

            if(len(set(curr_arr)) == 3):
                count += 1
        
        return count