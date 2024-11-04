import time
import random

# Directions: Right, Down, Left, Up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class TremauxSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[0 for _ in range(self.cols)] for _ in range(self.rows)]  # Track visits (0: unvisited, 1: visited once, 2: visited twice)
        self.path = []  # Record of the path taken to reach the goal

    def is_valid(self, x, y):
        # Check if within bounds and is an open cell (0)
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] == 0

    def solve(self, start, end):
        # Reset path and visited markers for a fresh solve
        self.path = []
        self.visited = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        # Start the recursive solving process
        if self._solve_recursive(start[0], start[1], end[0], end[1]):
            return self.path
        else:
            return []  # Return empty if no path found

    def _solve_recursive(self, x, y, end_x, end_y):
        # Mark the current cell as visited
        self.visited[x][y] += 1
        self.path.append((x, y))

        # Base case: If the current cell is the destination
        if (x, y) == (end_x, end_y):
            return True

        # Shuffle directions to randomize the path choice
        directions = random.sample(DIRECTIONS, len(DIRECTIONS))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # If the next cell is valid, not fully visited
            if self.is_valid(nx, ny) and self.visited[nx][ny] < 2:
                if self._solve_recursive(nx, ny, end_x, end_y):
                    return True  # Solution found

        # If all directions are blocked, backtrack
        self.path.pop()  # Remove the last cell from the path
        self.visited[x][y] += 1  # Mark as dead end if revisited
        return False  # Return to previous call if no path found from here

def runner(maze, start, end):
    startTime = time.perf_counter()
    solver = TremauxSolver(maze)
    path = solver.solve(start, end)
    endTime = time.perf_counter()
    tekken = endTime - startTime

    return path, tekken
