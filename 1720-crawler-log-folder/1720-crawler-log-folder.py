class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []

        for i in logs:
            if("/" in i and "../" not in i and "./" not in i):
                stack.append("d")

            elif(stack and "../" in i):
                stack.pop()

            else:
                pass

        
        return len(stack)