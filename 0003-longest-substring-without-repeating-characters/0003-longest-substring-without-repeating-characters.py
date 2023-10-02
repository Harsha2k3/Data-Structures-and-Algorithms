class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        end = 0
        max_length = 0
        seen = set()               # Empty Set

        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                max_length = max(max_length, end - start + 1)
                end += 1
            else:
                seen.remove(s[start])
                start += 1

        return max_length



        # Here say, current sliding window is abc
        # Now for checking and moving sliding window to make abca 
        # No need to check for bc, just check s[end] i.e, a is in 
        # seen set or not, if it is in seen set then start removing
        # the letters from back side until the letter a is removed
        # Now, bca is current sliding window
        # Continue this.