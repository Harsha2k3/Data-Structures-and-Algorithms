class Solution:
    def decodeMessage(self, k: str, m: str) -> str:

        l = []
        l_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        res = ""


        for i in k:
            if((i not in l) and (i != " ")):
                l.append(i)

        for i in range(len(m)):
            if(m[i] == " "):
                res += " "
            else:
                for j in range(len(l)):
                    if(m[i] == l[j]):
                        res += l_[j]

        return res