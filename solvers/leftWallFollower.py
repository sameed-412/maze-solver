import time

# Maze-solving using the Left-Hand Rule
# 0 - Open path, 1 - Wall

# Directions: Right, Down, Left, Up (clockwise order)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def leftHandRule(maze, start, end):
    start_time = time.perf_counter()
    x, y = start  # Current position
    direction = 0  # Starting facing 'Right' (index in DIRECTIONS)
    path = [(x, y)]  # Store path

    # Function to turn left
    def turn_left(d):
        return (d - 1) % 4

    # Function to turn right
    def turn_right(d):
        return (d + 1) % 4

    # Function to check if a cell is open
    def is_open(nx, ny):
        return 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0

    while (x, y) != end:
        # Try turning left first
        left_dir = turn_left(direction)
        nx, ny = x + DIRECTIONS[left_dir][0], y + DIRECTIONS[left_dir][1]
        
        if is_open(nx, ny):
            # Move to the cell on the left
            direction = left_dir
            x, y = nx, ny
            path.append((x, y))
        else:
            # If left is blocked, try moving forward
            nx, ny = x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1]
            if is_open(nx, ny):
                x, y = nx, ny
                path.append((x, y))
            else:
                # If forward is blocked, turn right
                direction = turn_right(direction)
                
    end_time = time.perf_counter()
    time_taken = end_time - start_time
    return path, time_taken
