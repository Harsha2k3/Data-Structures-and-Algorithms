"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root:
            root.next = None
        
        def dfs(root , isLeft , isRight , p):

            if not root:
                return
            
            if root.left:
                root.left.next = root.right
            
            
            if isRight:
                if p and p.next:
                    root.next = p.next.left
                else:
                    if root and p:
                        root.next = p.next

            dfs(root.left , True , False , root)
            dfs(root.right , False , True , root)

            return root

        return dfs(root , True , True , None)