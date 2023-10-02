class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head
        l = 1

        while(temp.next):
            temp = temp.next
            l += 1

        if(l == 1):
            return None
        
        if(n == 1):
            temp = head
            for i in range(l-2):      # For grabbing last but one node
                temp = temp.next
            temp.next = None
            tail = temp
        
        elif(n == l):
            temp = head
            for i in range(1):           # For grabbing second node
                temp = temp.next
            head.next = None
            head = temp

        
        else:
            temp = head
            for i in range(l-n-1):
                temp = temp.next
            
            if(temp and temp.next):
                temp.next = temp.next.next

        return head