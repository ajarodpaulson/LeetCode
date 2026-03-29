1class Solution:
2    def findCenter(self, edges: List[List[int]]) -> int:
3        visited_nodes = set()
4        for edge in edges:
5            u = edge[0]
6            v = edge[1]
7            if u in visited_nodes:
8                return u
9            if v in visited_nodes:
10                return v
11            visited_nodes.add(u)
12            visited_nodes.add(v)
13        