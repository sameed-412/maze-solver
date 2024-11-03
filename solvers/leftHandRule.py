import time
# Maze-solving using the Left-Hand Rule
# 0 - Open path, 1 - Wall

# Directions: Up, Left, Down, Right (clockwise order)
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
def leftHandRule(maze, start, end):
    start_time = time.perf_counter()
    x, y = start  # Current position
    direction = 0  # Starting facing 'Up' (index in DIRECTIONS)
    path = [(x, y)]  # Store path

    # Function to turn left
    def turn_left(d):
        return (d + 1) % 4

    # Function to turn right
    def turn_right(d):
        return (d - 1) % 4

    # Function to check if a cell is open
    def is_open(nx, ny):
        return 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0

    while (x, y) != end:
        # Try turning left
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
    return path,time_taken

def runner():
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)  # Starting point (top-left corner)
    end = (0, 3)  # Exit point (top-middle 0)
    path,time = leftHandRule(maze, start, end)

    print(f"path:{path}")
    print(f"time:{time:.20f}")


# runner()