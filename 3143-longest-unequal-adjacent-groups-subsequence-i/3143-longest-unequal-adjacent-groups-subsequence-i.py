class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        
        res = []
        
        for i in range(n):
            if(i == 0 or groups[i] != groups[i-1]):
                res.append(words[i])
        
        return res