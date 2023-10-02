class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        temp = head

        while(temp):
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        head = prev

        return head