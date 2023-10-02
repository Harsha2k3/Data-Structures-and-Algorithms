class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        temp = head
        ll = ListNode(0)
        d = ll

        while(temp):
            if(temp.val < x):
                ll.next = ListNode()
                ll = ll.next
                ll.val = temp.val        
            temp = temp.next
        
        temp = head
        while(temp):
            if(temp.val >= x):
                ll.next = ListNode()
                ll = ll.next
                ll.val = temp.val    
            temp = temp.next

        return d.next