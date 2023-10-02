class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        temp = head
        l = 1

        while(temp != None):
            temp = temp.next
            l += 1
        
        temp1 = head

        for i in range(k-1):
            temp1 = temp1.next
        
        temp2 = head

        for i in range(l-1-k):
            temp2 = temp2.next

        
        temp1.val,temp2.val = temp2.val,temp1.val

        return head


        # However, you can make it slightly more efficient by avoiding the second traversal to find temp2. You can achieve this by maintaining two pointers separated by a distance of k-1 nodes, and then moving both pointers until one of them reaches the end of the list. This would reduce the time complexity to O(n) without the need for a second traversal.