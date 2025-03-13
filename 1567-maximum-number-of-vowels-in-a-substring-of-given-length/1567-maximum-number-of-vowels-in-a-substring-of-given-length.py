class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        v = "aeiou"

        start = 0
        count = 0

        res = float("-inf")

        for end in range(len(s)):
            if s[end] in v: count += 1 

            if end - start + 1 == k:
                res = max(res , count)
                if s[start] in v: count -= 1 
                start += 1

        return res 






#         vowels = set(["a", "e", "i", "o", "u"])

#         curr_arr = s[:k]
#         max_count = 0
#         count = 0

#         for char in curr_arr:
#             if char in vowels:
#                 count += 1

#         max_count = count

#         for i in range(1, len(s) - k + 1):
#             if s[i - 1] in vowels:
#                 count -= 1
#             if s[i + k - 1] in vowels:
#                 count += 1

#             max_count = max(max_count, count)
#             curr_arr = s[i : k + i]

#         return max_count


# # In each iteration, check if the character at index i - 1 (the character leaving the window) is a vowel. If it is, decrement the count by 1 since it's no longer in the current substring.




# # Initialize the current window to s[:k]
# # Count the number of vowels in s[:k] and store it in count
# # Assign that count in max_count initially
# # Now move the window using a for loop
# # In each ireration,
# # s[i-1] leaves the window
# # s[i+k-1] eneters the window
# # As s[i-1] leaves the window,if s[i-1] is vowel the count -= 1
# # As s[i+k-1] enters the window,if s[i+k-1] is vowel the count += 1
# # In each iteration max_count = max(max_count,count)