from random import choice, shuffle

# Constants
cols, rows = 19, 19  # Size of the maze

# Directions for moving in the maze
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left

# Maze initialization
maze = [[1 for _ in range(cols)] for _ in range(rows)]

def generate_maze(x, y):
    maze[y][x] = 0  # Mark the current cell as an open path
    shuffle(DIRECTIONS)  # Randomly order the directions

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx * 2, y + dy * 2  # Calculate the neighbor's position

        # Check if the neighbor is within bounds and not visited
        if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] == 1:
            maze[y + dy][x + dx] = 0  # Remove the wall between the current and neighbor cell
            generate_maze(nx, ny)  # Recursively visit the neighbor

generate_maze(0, 0)
# Start generating the maze from the top-left corner
def return_maze():
    return maze

# Print the maze as a matrix
def printmaze():
    for row in maze:
        print(row)