class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        res = 0

        seats.sort()
        students.sort()

        for i in range(len(seats)):
            if(seats[i]-students[i] < 0):
                res += -1*(seats[i]-students[i])
            else:
                res += seats[i]-students[i]

        return res