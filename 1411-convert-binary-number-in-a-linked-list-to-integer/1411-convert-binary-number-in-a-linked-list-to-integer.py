class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        temp = head
        l = 1

        while(temp.next):
            temp = temp.next
            l += 1

        i = l-1
        res = 0

        temp = head

        while(temp):
            if(temp.val == 1):
                res += 2**(i)
            i -= 1
            temp = temp.next

        return res