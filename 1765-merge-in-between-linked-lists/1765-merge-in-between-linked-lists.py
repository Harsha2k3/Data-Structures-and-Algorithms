class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        temp = list1

        for i in range(a-1):
            temp = temp.next

        ab = temp               # ab ==> a's before node

        temp1 = list1

        for i in range(b):
            temp1 = temp1.next

        b = temp1               # b ==> b's node
        ba = b.next             # ba ==> b's after node

        ab.next = list2

        t = list2

        while(t.next):
            t = t.next

        t.next = ba

        return list1