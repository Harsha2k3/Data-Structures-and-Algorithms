class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        res = 0

        start = 0

        v = "aeiou"

        vowel_set = set()

        for end in range(len(word)):

            if word[end] in v and (end == 0 or ord(word[end]) >= ord(word[end - 1])):
                vowel_set.add(word[end])
                if len(vowel_set) == 5:
                    res = max(res , end - start + 1)

            if word[end] not in v or (end != 0 and ord(word[end]) < ord(word[end - 1])):
                vowel_set = set(word[end])
                start = end

        return res