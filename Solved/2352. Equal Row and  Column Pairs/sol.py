from typing import List


class Solution:
    def go_through_columns(self, grid):
        sums = {}
        n = len(grid)
        for j in range(n):
            current_sum = ""
            for i in range(n):
                current_sum += "_" + str(grid[i][j])
            sums[current_sum] = sums.get(current_sum, 0) + 1
        return sums

    def go_through_rows(self, grid):
        sums = {}
        for row in grid:  # Directly iterate through rows
            current_sum = ""
            for cell in row:
                current_sum += "_" + str(cell)
            sums[current_sum] = sums.get(current_sum, 0) + 1
        return sums

    def combine_columns(self, columns: dict, rows: dict):
        pairs = 0
        for key, val in rows.items():
            value_column = columns.get(key)
            if value_column:
                pairs += val * value_column
        return pairs

    def equalPairs(self, grid: List[List[int]]) -> int:
        row_patterns = self.go_through_rows(grid)
        col_patterns = self.go_through_columns(grid)
        return self.combine_columns(row_patterns, col_patterns)


if __name__ == "__main__":
    sol = Solution()
    s = sol.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]])
    print(s)
