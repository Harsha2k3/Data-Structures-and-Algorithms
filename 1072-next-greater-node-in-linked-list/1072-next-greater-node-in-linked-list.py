class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        temp = head

        l = []
        stack = []         # Monotonic Stack

        while(temp):
            l.append(temp.val)
            temp = temp.next

        for i in range(len(l)):
            k = l[len(l)-i-1]
            if(stack and stack[-1] > l[len(l)-i-1]):
                l[len(l)-i-1] = stack[-1]
            elif(stack and stack[-1] <= l[len(l)-i-1]):
                while(stack and stack[-1] <= l[len(l)-i-1]):
                    stack.pop()
                if(stack): l[len(l)-i-1] = stack[-1]
                elif(stack == []): l[len(l)-i-1] = 0

            elif(stack == []):
                l[len(l)-i-1] = 0

            stack.append(k)

        return l