class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s = list(s)
        t = list(t)

        s_stack = []
        t_stack = []

        for i in s:
            if(i.isalpha()):
                s_stack.append(i)
            if(s_stack and i == "#"):
                s_stack.pop()

        for i in t:
            if(i.isalpha()):
                t_stack.append(i)
            if(t_stack and i == "#"):
                t_stack.pop()

        return s_stack == t_stack