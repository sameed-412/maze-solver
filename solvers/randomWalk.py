import random
import time

# Define the maze as a 2D list, where 1 represents walls and 0 represents open paths

# Define possible moves (down, up, right, left)
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def whatIsBroDoing(maze, start, end, max_steps=10000):
    current_position = start
    path = [current_position]
    steps = 0
    start_time = time.perf_counter()
    
    while current_position != end and steps < max_steps:
        steps += 1
        next_move = random.choice(moves)
        
        # Calculate new position based on the random move
        new_position = (current_position[0] + next_move[0], current_position[1] + next_move[1])
        
        # Check if the new position is within bounds and not a wall
        if (0 <= new_position[0] < len(maze) and
            0 <= new_position[1] < len(maze[0]) and
            maze[new_position[0]][new_position[1]] == 0):
            current_position = new_position
            path.append(current_position)
            
            # Stop if we reach the end
            if current_position == end:
                end_time = time.perf_counter()
                tekken = end_time - start_time
                return path, tekken
            
    print("Random walk did not reach the exit.")
    end_time = time.perf_counter()
    tekken = end_time - start_time
    return path, tekken