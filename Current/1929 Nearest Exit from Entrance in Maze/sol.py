from typing import List
from collections import deque


class Solution:
    def is_exit(self, next_row, next_col, rows, cols) -> bool:
        if (
            next_row == 0
            or next_row == rows - 1
            or next_col == 0
            or next_col == cols - 1
        ):
            return True
        return False

    def is_valid_step(self, next_row, next_col, rows, cols, maze):
        if (
            0 <= next_row < rows
            and 0 <= next_col < cols
            and maze[next_row][next_col] == "."
        ):
            return True
        return False

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])

        queue = deque()
        queue.append((entrance[0], entrance[1], 0))

        # Mark entrance as visited
        maze[entrance[0]][entrance[1]] = "+"

        directions = [
            (1, 0),  # down
            (-1, 0),  # up
            (0, 1),  # right
            (0, -1),  # left
        ]

        while queue:
            curr_row, curr_col, steps = queue.popleft()

            for dx, dy in directions:
                next_row = curr_row + dx
                next_col = curr_col + dy

                if self.is_valid_step(next_row, next_col, rows, cols, maze):
                    if self.is_exit(next_row, next_col, rows, cols):
                        return steps + 1
                    maze[next_row][next_col] = "+"
                    queue.append((next_row, next_col, steps + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()
    maze = [
        ["+", ".", "+", "+", "+", "+", "+"],
        ["+", ".", "+", ".", ".", ".", "+"],
        ["+", ".", "+", ".", "+", ".", "+"],
        ["+", ".", ".", ".", "+", ".", "+"],
        ["+", "+", "+", "+", "+", ".", "+"],
    ]
    entrance = [0, 1]
    print(sol.nearestExit(maze=maze, entrance=entrance))
