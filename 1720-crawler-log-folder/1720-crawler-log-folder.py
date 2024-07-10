class Solution:
    def minOperations(self, logs: List[str]) -> int:

        # If we encounter "x/" ==> push file on to the stack
        # If we encounter "../" ==> pop from the stack
        # If we encounter "./" ==> Do nothing
        # return len(stack)

        stack = []

        for i in logs:
            if("/" in i and "../" not in i and "./" not in i):
                stack.append("d")

            elif(stack and "../" in i):
                stack.pop()

            else:
                pass

        
        return len(stack)