class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        al = []
        bl = []
        cl = []

        for i in bin(a)[2:]:
            al.append(i)
        
        for i in bin(b)[2:]:
            bl.append(i)
        
        for i in bin(c)[2:]:
            cl.append(i)
        
        m = max(len(al),len(bl),len(cl))

        while(len(al) < m):
            al = ["0"] + al
        
        while(len(bl) < m):
            bl = ["0"] + bl

        while(len(cl) < m):
            cl = ["0"] + cl

        
        count = 0

        for i in range(len(cl)):
            if(cl[i] == "0"):
                if(al[i] == "1"):
                    count += 1
                if(bl[i] == "1"):
                    count += 1
            elif(cl[i] == "1"):
                if(al[i] == "1"):
                    continue
                if(bl[i] == "1"):
                    continue
                else:
                    count += 1
            
        return count