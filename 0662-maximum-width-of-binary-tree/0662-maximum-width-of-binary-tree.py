from queue import Queue

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Do a level-order traversal and assign positions to each node

        if not root:
            return 0

        res = 0

        q = Queue()

        q.put((root , 0))   # (root , pos)

        while not q.empty():

            size = q.qsize()

            fp = q.queue[0][1]     # Front position of that level

            first = None
            last = None

            for i in range(size):

                curr_pos = q.queue[0][1] - fp

                node = q.queue[0][0]

                q.get()

                if i == 0:
                    first = curr_pos

                if i == size - 1:
                    last = curr_pos


                if node.left:
                    q.put((node.left , curr_pos * 2 + 1))

                if node.right:
                    q.put((node.right , curr_pos * 2 + 2))

            res = max(res , last - first + 1)

        return res