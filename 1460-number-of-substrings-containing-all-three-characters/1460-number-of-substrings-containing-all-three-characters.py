class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        # count = 0

        # a , b , c = -1 , -1 , -1

        # # Stores indices at where those char's are last seen
        # h = {i : -1 for i in set(s)}    

        # if "a" in s:
        #     a = 1
        
        # if "b" in s:
        #     b = 1

        # if "c" in s:
        #     c = 1
        

        # for i in range(len(s)):
        #     h[s[i]] = i

        #     if((a == 1 and h["a"] != -1) and (b == 1 and h["b"] != -1) and (c == 1 and h["c"] != -1)):
        #         count += 1 + min(h["a"] , h["b"] , h["c"])

        # return count

        # # If a string has all the 3 alphabets then, 
        # # the no.of strings till there which have all 3
        # # alphabets will be 1(this one) + no.of alphabets 
        # # before this string

        # # Here, say a ==> a = 0 , b = -1 , c = -1
        # # b ==> a = 0 , b = 1 , c = -1
        # # c ==> a = 0 , b = 1 , c = 2
        # # Now, a,b and c != -1 ==> count = 1 string

        # # a ==> a = 3 , b = 1 , c = 2
        # # Now, a,b and c != -1 ==> count = count + (1 + alphabets before bca)
        # # i.e, count = 1 + (1 + 1) = 3 strings
        # # Becoz, bca has all strings then if we keep any other extra
        # # alphabet in it even then it will have 3 alphabets
        # # in those strings

        # (Or)

        # Same thing can also be done like this 

        count, start = 0, 0

        h = {i : 0 for i in "abc"}
        
        for end in range(len(s)):
            h[s[end]] += 1
            
            while h["a"] and h["b"] and h["c"]:
                h[s[start]] -= 1
                start += 1
            
            count += start
            
        return count