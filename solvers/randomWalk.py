import random
import time

def whatIsBroDoing(maze, start, end, max_steps=1000):
    x, y = start
    path = [(x, y)] # Store the path taken
    visited = set() # Keep track of visited cells to avoid revisiting

    # Define directions for moving: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    steps = 0
    while (x, y) != end and steps < max_steps:
        visited.add((x, y))
        possible_moves = []

        # Check for all possible moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited):
                possible_moves.append((nx, ny))

        if possible_moves:
            # Randomly select the next move
            x, y = random.choice(possible_moves)
            path.append((x, y))
        else:
            # Dead end, backtrack
            path.pop()
            if path:
                x, y = path[-1]
            else:
                # No path found
                return []

        steps += 1

    # Check if reached the end
    if (x, y) == end:
        return path
    else:
        return []  # Return empty path if end wasn't reached within max_steps

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
    path = whatIsBroDoing(maze, start, end)
    endTime = time.perf_counter()
    tekken = f"{(endTime - startTime):.20f}"

    return path, tekken

print(runner())