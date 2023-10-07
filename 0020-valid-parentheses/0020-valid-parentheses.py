class Solution:
    def isValid(self, s: str) -> bool:


        # If we encounter a open bracket, we just push it on to the stack

        # If we encounter a closing bracket then we check if top of stack contains same type of the closing bracket or not, if it is, then we pop the top most item (i.e, corresponding opening bracket)

        # If we continue doing this, the stack gets empty for a valid s. 

        stack = []

        for i in s:
            if len(stack)==0 and (i==')' or i=='}' or i==']'):
                return False
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif i==')' and stack[-1]=='(':
                stack.pop()
            elif i=='}' and stack[-1]=='{':
                stack.pop()
            elif i==']' and stack[-1]=='[':
                stack.pop()
            else:
                return False
                
        if len(stack):
            return False
        else:
            return True


        # ([)] ==> This is not valid, last opend one(i.e, "[") should be closed first than the 1st opened one(i.e, "[") i.e, ([])