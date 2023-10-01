import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = head
        temp2 = head.next

        while(temp2):
            temp = ListNode(math.gcd(temp1.val,temp2.val)) # It will create a new node with a value gcd of two numbers
            temp.next = temp2
            temp1.next = temp
            
            temp1 = temp1.next.next
            temp2 = temp2.next
        
        return head