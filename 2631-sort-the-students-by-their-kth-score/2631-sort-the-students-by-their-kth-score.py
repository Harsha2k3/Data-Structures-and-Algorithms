class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        l = []
        res = []

        for i in range(len(score)):
            l.append([score[i][k],i])

        l = sorted(l, key=lambda x: x[0],reverse = True)

        for i in range(len(l)):
            res.append(score[l[i][1]])

        return res