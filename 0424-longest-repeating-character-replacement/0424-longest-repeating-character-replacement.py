class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        h = {i : 0 for i in set(s)}
        start = 0
        max_len = -10000000

        for end in range(len(s)):
            h[s[end]] += 1

            while (end - start + 1) - max(h.values()) > k:
                h[s[start]] -= 1
                start += 1

            max_len = max(max_len , end - start + 1)

        return max_len

        # ABABBA
        # Hashmap ==> Stores freq's of char's in that window
        # Idea ==> In every window the char's other than highest freq char's are replaced inorder to achieve longest repeating char(of highest freq char of that window) sub-array
        # Say window = ABA ==> A is most frequent, so replace other char's in window with most freq char(i.e, A)
        # Expand the window till no.of replacements <= k
        # No.of replacements = window length - max freq of a char in that window
        # Expand till window length - max freq <= k
        # When the condition fails, shrink the window until window length - max freq <= k