class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter_values = []
        for row_idx, row in enumerate(grid):
            for cell_idx, cell_value in enumerate(row):
                position = (row_idx, cell_idx)
                if not self.getIsIsland(position, grid):
                    continue
                curr_perimeter_value = 4
                if self.getHasNeighbouringIsland(position, grid, "left"):
                    curr_perimeter_value -= 1
                if self.getHasNeighbouringIsland(position, grid, "right"):
                    curr_perimeter_value -= 1
                if self.getHasNeighbouringIsland(position, grid, "above"):
                    curr_perimeter_value -= 1
                if self.getHasNeighbouringIsland(position, grid, "below"):
                    curr_perimeter_value -= 1
                perimeter_values.append(curr_perimeter_value)

        return sum(perimeter_values)

    def getIsIsland(self, position, grid):
        return grid[position[0]][position[1]]

    def getHasNeighbouringIsland(self, position, grid, neighbourRelativeLocation):
        match (neighbourRelativeLocation):
            case "left":
                neighbour_position = (position[0], position[1] - 1)
                if self.getIsNeighbourPositionOOB(neighbour_position, grid):
                    return False
                return self.getIsIsland(neighbour_position, grid)
            case "right":
                neighbour_position = (position[0], position[1] + 1)
                if self.getIsNeighbourPositionOOB(neighbour_position, grid):
                    return False
                return self.getIsIsland(neighbour_position, grid)
            case "above":
                neighbour_position = (position[0] - 1, position[1])
                if self.getIsNeighbourPositionOOB(neighbour_position, grid):
                    return False
                return self.getIsIsland(neighbour_position, grid)
            case "below":
                neighbour_position = (position[0] + 1, position[1])
                if self.getIsNeighbourPositionOOB(neighbour_position, grid):
                    return False
                return self.getIsIsland(neighbour_position, grid)

    def getIsNeighbourPositionOOB(self, position, grid):
        grid_width = len(grid[0])
        grid_height = len(grid)

        return (
            position[0] >= grid_height
            or position[0] < 0
            or position[1] >= grid_width
            or position[1] < 0
        )
