1import copy
2
3class Solution:
4    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
5        height_of_grid = len(grid)
6        width_of_grid = len(grid[0])
7        visited_nodes = self.build_visited_nodes(height_of_grid, width_of_grid)
8        max_island_area = 0
9
10        for y, row in enumerate(grid):
11            for x, node in enumerate(row):
12                # the coordinate of a node is x,y
13                if visited_nodes[y][x]:
14                    continue
15
16                if node == 0:
17                    continue
18
19                nodes_in_current_island = self.explore_island(
20                    visited_nodes, grid, [y, x]
21                )
22                max_island_area = max(max_island_area, nodes_in_current_island)
23
24        return max_island_area
25
26    def explore_island(self, visited_nodes, grid, starting_coords):
27        y = starting_coords[0]
28        x = starting_coords[1]
29
30        if y < 0 or y > (len(grid) - 1):
31            return 0
32
33        if x < 0 or x > (len(grid[0]) - 1):
34            return 0
35
36        if visited_nodes[y][x]:
37            return 0
38
39        visited_nodes[y][x] = True
40
41        if grid[y][x] == 0:
42            return 0
43
44        result_left = self.explore_island(visited_nodes, grid, [y, x - 1])
45        result_right = self.explore_island(visited_nodes, grid, [y, x + 1])
46        result_up = self.explore_island(visited_nodes, grid, [y - 1, x])
47        result_down = self.explore_island(visited_nodes, grid, [y + 1, x])
48
49        return 1 + result_left + result_right + result_up + result_down
50
51    def build_visited_nodes(self, height, width) -> List[List[bool]]:
52        row = [False] * width
53
54        grid = []
55        for i in range(height):
56            new_row = row[:]
57            grid.append(new_row)
58        return grid
59