class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        stream = [i for i in range(1,n+1)]
        res = []
        r = []

        j = 0
        for i in range(len(stream)):
            if(stream[i] == target[j]):
                res.append("Push")
                r.append(target[j])
                j += 1
            else:
                res.append("Push")
                res.append("Pop")

            if(target == r):
                break
        
        return res