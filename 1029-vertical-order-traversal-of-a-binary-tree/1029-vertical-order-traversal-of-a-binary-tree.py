from collections import defaultdict , deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Just mark them traversing by BFS 

        node_list = []

        todo = deque([(root , 0 , 0)])    # root , vertical , level

        while todo:

            node , v , l = todo.popleft()

            if node:
                node_list.append((v , l , node.val))
                todo.append((node.left , v - 1 , l + 1))
                todo.append((node.right , v + 1 , l + 1))
        
        node_list.sort()

        res = defaultdict(list)

        for v , l , node in node_list:
            res[v].append(node)
        
        return [res[i] for i in sorted(res.keys())]