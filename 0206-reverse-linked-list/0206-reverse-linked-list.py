# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         prev = None
#         temp = head

#         def rec():

#             nonlocal temp, prev

#             if(not temp):
#                 return prev

#             else:
#                 nxt = temp.next
#                 temp.next = prev
#                 prev = temp
#                 temp = nxt
#                 return rec()

#         return rec()

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        temp = head

        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        
        return prev