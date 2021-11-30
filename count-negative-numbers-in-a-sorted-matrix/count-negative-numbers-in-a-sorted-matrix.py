class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                num = grid[row][col]
                if num < 0:
                    c +=1
        return c
        