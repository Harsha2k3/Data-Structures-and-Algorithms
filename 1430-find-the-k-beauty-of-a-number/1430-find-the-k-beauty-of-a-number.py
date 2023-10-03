class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        sub_arr = str(num)[:k]
        count = 0

        # if(num % int(sub_arr) == 0):
        #     count += 1

        for i in range(len(str(num))-k+1):
            sub_arr = str(num)[i:k+i]

            if(int(sub_arr) != 0 and num % int(sub_arr) == 0):
                count += 1
        
        return count