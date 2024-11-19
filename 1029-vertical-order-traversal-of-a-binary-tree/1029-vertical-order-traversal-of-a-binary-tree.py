from collections import defaultdict , deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Just mark vertical and level by traversing through BFS 
        # Just store all the tuples of (vertical , level , value of root) by BFS
        
        node_list = []

        q = deque([(root , 0 , 0)])    # root , vertical , level

        while q:

            for i in range(len(q)):

                node , v , l = q.popleft()

                node_list.append((v , l , node.val))

                if node.left:
                    q.append((node.left , v - 1 , l + 1))

                if node.right:
                    q.append((node.right , v + 1 , l + 1))

        print(node_list)
        
        node_list.sort()

        print(node_list)

        res = defaultdict(list)

        for v , l , node in node_list:
            res[v].append(node)

        print(res)
        
        return [res[i] for i in sorted(res.keys())]