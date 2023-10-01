class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        sum = 0

        ll_head = ListNode()
        h = ll_head

        temp = head.next

        while(temp):
            if(temp.val != 0):
                sum += temp.val       
            else:
                ll_head.val = sum
                if(temp.next):
                    ll_head.next = ListNode()
                    ll_head = ll_head.next
                    sum = 0
            temp = temp.next
        
        return h