import heapq
import time

def dorkStronk(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    # Distance dictionary, initialized with infinity
    distances = { (r, c): float('inf') for r in range(rows) for c in range(cols) }
    distances[start] = 0  # Starting point has distance 0

    # Priority queue to get the cell with the smallest distance
    priority_queue = [(0, start)]  # (distance, (row, col))
    came_from = {}  # To track the path

    # Directions for moving: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while priority_queue:
        current_distance, (current_row, current_col) = heapq.heappop(priority_queue)

        # If we reach the end, reconstruct the path
        if (current_row, current_col) == end:
            path = []
            while (current_row, current_col) != start:
                path.append((current_row, current_col))
                current_row, current_col = came_from[(current_row, current_col)]
            path.append(start)
            return path[::-1]  # Return reversed path from start to end

        # Explore neighbors
        for dr, dc in directions:
            neighbor_row, neighbor_col = current_row + dr, current_col + dc
            # Check boundaries and if the neighbor is a path (0 in maze)
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and maze[neighbor_row][neighbor_col] == 0:
                new_distance = current_distance + 1  # Each move costs 1
                if new_distance < distances[(neighbor_row, neighbor_col)]:
                    distances[(neighbor_row, neighbor_col)] = new_distance
                    came_from[(neighbor_row, neighbor_col)] = (current_row, current_col)
                    heapq.heappush(priority_queue, (new_distance, (neighbor_row, neighbor_col)))

    return []  # Return empty path if there's no way to reach the end

def runner():
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)

    startTime = time.perf_counter()
    path = dorkStronk(maze, start, end)
    endTime = time.perf_counter()
    tekken = f"{(endTime - startTime):.20f}"

    return path, tekken

print(runner())