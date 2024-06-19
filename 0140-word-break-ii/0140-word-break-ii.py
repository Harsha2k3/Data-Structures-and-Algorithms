class Solution:
    def wordBreak(self, s: str, dictionary: List[str]) -> List[str]:
        
        word_set = set(dictionary)
        res = []

        @lru_cache(None)
        def backtrack(index):
            if index == len(s):
                return [[]]  # Return a list containing an empty list to signify a valid end
            
            sentences = []
            for j in range(index , len(s)):
                if s[index : j + 1] in word_set:
                    for subsentence in backtrack(j + 1):
                        sentences.append([s[index : j + 1]] + subsentence)
            
            return sentences

        complete_sentences = backtrack(0)
        for sentence in complete_sentences:
            res.append(" ".join(sentence))
        
        return res