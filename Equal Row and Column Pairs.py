class Solution:
    def equalPairs(self, grid):
        n = len(grid)

      
        row_count = {}

        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1

        count = 0

       
        for c in range(n):
            col = []

            for r in range(n):
                col.append(grid[r][c])

            col_tuple = tuple(col)

            count += row_count.get(col_tuple, 0)

        return count
