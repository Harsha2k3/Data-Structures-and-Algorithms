class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        element_count = defaultdict(int)

        for edge in edges:
            for element in edge:
                element_count[element] += 1
        
        common_elements = [element for element, count in element_count.items() if count == len(edges)]
        
        return common_elements[0]