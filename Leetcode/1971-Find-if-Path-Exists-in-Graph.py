class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = self.makeAdjacencyList(n, edges)
        
        stack = []
        visited = set()

        stack.append(source)

        while (len(stack)):
            curr_vertex = stack.pop()

            if curr_vertex in visited:
                continue
            
            visited.add(curr_vertex)

            if curr_vertex == destination:
                return True

            for adjacent_vertex in adjacency_list[curr_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)

        return False

    def makeAdjacencyList(self, n, edges):
        adjacency_list = {}
        
        for i in range(n):
            adjacency_list[i] = []

        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        return adjacency_list
            
'''
time: 
to make the adjacency list, O(edges)
and the dfs in the worst case can look at every edge for every vertex, so O(edges + vertices)

space:
the stack can store O(n) vertices since we do not add vertices that have already been visited
the adjacency list stores all of the vertices and their edges, so space is O(vertices + edges)
'''