import time

# Define directions for movement: (dx, dy)
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Function to turn right
def turn_right(direction):
    return (direction + 1) % 4

# Function to turn left
def turn_left(direction):
    return (direction - 1) % 4

# Maze dimensions
rows = 19
cols = 19



# Function to solve maze using right-hand following
def solve_maze(maze, start, end):
    path = []
    current_pos = start
    direction = DOWN  # Initial direction (can vary based on maze design)
    
    # print("The Path is:")
    startTime = time.perf_counter()
    while current_pos != end:
        path.append(current_pos)
        # Print each step with arrow if it's not the last step
        # if current_pos != end:
            # print(current_pos, end=" -> ")
        
        x, y = current_pos
        
        # Check right-hand cell
        right_dir = turn_right(direction)
        rx, ry = x + directions[right_dir][0], y + directions[right_dir][1]
        
        # If right-hand cell is open, turn right and move forward
        if 0 <= rx < rows and 0 <= ry < cols and maze[rx][ry] == 0:
            direction = right_dir
            current_pos = (rx, ry)
        else:
            # Otherwise, check if forward is open
            fx, fy = x + directions[direction][0], y + directions[direction][1]
            if 0 <= fx < rows and 0 <= fy < cols and maze[fx][fy] == 0:
                current_pos = (fx, fy)
            else:
                # If forward is blocked, turn left
                direction = turn_left(direction)
    
    # Print the final destination
    # print(end)  # Print the last step without arrow
    path.append(end)
    endTime = time.perf_counter()
    time_taken = endTime - startTime
    return path,time_taken

# Run the algorithm and time it
def timer(maze,start,end):
    
    path = solve_maze(maze, start, end)
    endTime = time.perf_counter()
    taken = f"{(endTime - startTime):.20f}"
    return path, taken
