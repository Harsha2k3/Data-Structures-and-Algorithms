from queue import Queue

class Codec:
    def serialize(self, root):

        # Use BFS and convert into string

        if not root:
            return ""

        s = ""

        q = Queue()

        q.put(root)

        while not q.empty():

            cur_node = q.get()

            if not cur_node:
                s += "#,"
            else:
                s += str(cur_node.val) + ","
                q.put(cur_node.left)
                q.put(cur_node.right)

        return s

    def deserialize(self , data):

        # Construct the tree again from string constructed from BFS

        # https://www.youtube.com/watch?v=-YbXySKJsX8&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=38
        # Watch from 4:34 to 7:34

        if not data:
            return None

        q = Queue()

        tokens = data.split(',')

        root_val = int(tokens.pop(0))
        root = TreeNode(root_val)
        q.put(root)

        while not q.empty():

            node = q.get()

            left_val = tokens.pop(0)

            if left_val != "#":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.put(left_node)

            right_val = tokens.pop(0)

            if right_val != "#":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.put(right_node)

        return root