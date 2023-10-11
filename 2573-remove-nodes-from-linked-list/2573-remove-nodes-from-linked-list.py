class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l = []
        monotonic_stack = []

        temp = head

        while(temp):
            l.append(temp)
            temp = temp.next

        for i in range(len(l)):

            if(monotonic_stack and monotonic_stack[-1].val <= l[len(l)-i-1].val):
                monotonic_stack.append(l[len(l)-i-1])
            
            if(monotonic_stack == []):
                monotonic_stack.append(l[len(l)-i-1])


        new_head = monotonic_stack[-1]

        for i in range(len(monotonic_stack)-1):
            monotonic_stack[len(monotonic_stack)-i-1].next = monotonic_stack[len(monotonic_stack)-i-2]

        return new_head