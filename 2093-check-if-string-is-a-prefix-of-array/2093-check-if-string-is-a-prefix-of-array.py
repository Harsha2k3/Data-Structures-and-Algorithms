class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        cs = ""

        for r in words:
            cs += r
            if cs == s:
                return True
            if len(cs) > len(s) or cs != s[:len(cs)]:
                return False
        
        return False