class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        # element_count = defaultdict(int)

        # for i , j in edges:
        #     element_count[i] += 1
        #     element_count[j] += 1
        
        # common_elements = [element for element, count in element_count.items() if count == len(edges)]
        
        # return common_elements[0]

        # (Or)
        
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]