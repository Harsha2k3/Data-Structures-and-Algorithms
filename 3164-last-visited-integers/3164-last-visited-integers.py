class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        
        
        nums = []
        k = 0       # Number of Consecutive prev's
        res = []
        
        for i in range(len(words)):
            if(words[i].isdigit()):
                nums.append(int(words[i]))
                k = 0
            else:
                k += 1
                if(k <= len(nums)):
                    res.append(nums[::-1][k-1])
                else:
                    res.append(-1)
                    
        return res