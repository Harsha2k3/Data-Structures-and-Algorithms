class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        t = ""
        l = []

        for i in range(len(digits)):
            digits[i] = str(digits[i])

        for i in digits:
            t += i
        
        t = int(t)
        t = t+1
        t = str(t)

        for i in t:
            l.append(i)
        
        for i in range(len(l)):
            l[i] = int(l[i])

        return l