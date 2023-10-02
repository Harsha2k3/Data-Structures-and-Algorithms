class Solution:
    def romanToInt(self, s: str) -> int:
        l = ["I","V","X","L","C","D","M"]
        l_ = [1,5,10,50,100,500,1000]
        li = []
        sum = 0

        for i in range(len(s)):
            li.append(s[i])
        
        
        for i in range(len(li)):
            for j in range(len(l)):
                if(li[i] == l[j]):
                    sum = sum + l_[j]

        if("IV" in s):
            sum = sum - 2
        if("IX" in s):
            sum = sum - 2
        if("XL" in s):
            sum = sum - 20
        if("XC" in s):
            sum = sum - 20
        if("CD" in s):
            sum = sum - 200
        if("CM" in s):
            sum = sum - 200

        return sum