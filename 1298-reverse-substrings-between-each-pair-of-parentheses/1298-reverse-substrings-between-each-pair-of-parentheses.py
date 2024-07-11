class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            
            if char == ')':
                rev = ""
                
                while stack and stack[-1] != '(':
                    rev += stack.pop()
                    
                if stack:
                    stack.pop() 
                    
                for c in rev:
                    stack.append(c)
                    
            else:
                stack.append(char)
                
        return ''.join(stack)