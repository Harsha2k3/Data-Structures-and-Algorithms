class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        
        max_ = 0

        for i in range(len(s)):
            max_ = max(max_,len(s[i].split(" ")))
        
        return max_