# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy_ = dummy

        num1 = num2 = ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        res = str(int(num1) + int(num2))
        
        for i in res:
            dummy.next = ListNode(i)
            dummy = dummy.next

        return dummy_.next    