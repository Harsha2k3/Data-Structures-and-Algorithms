class Solution:
    def isPrefixOfWord(self, s: str, sw: str) -> int:
        
        l = s.split(" ")

        for i in range(len(l)):
            if l[i][0 : len(sw)] == sw:
                return i + 1
        
        return -1