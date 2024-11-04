import pygame

import generator  #this module generates the maze as a 2d matrix of 1's and 0's

#importing solving algorithms
from solvers import aStar , dikestruh , leftWallFollower , randomWalk , rightWallFollowing , tremaux

cols, rows = 19,19  # Size of the maze
tile = 25 # size of each block in the maze (in pixels)
pygame.init()
screen = pygame.display.set_mode((1500, 600))
subscreen = pygame.Surface((500, 500))  # maze is drawn on this subscreen
clock = pygame.time.Clock()

grey = pygame.Color("#77869e")
darkgrey = pygame.Color("#555657")
black = pygame.Color("Black")
indianred = pygame.Color("indianred2")

maze = generator.return_maze()  
x = tile
y = tile



def draw_maze(matrix , path = []):
    # Clear the subscreen before drawing
    subscreen.fill(grey)  # Fill with black or any background color
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            color = indianred if matrix[y][x] == 1 else grey
            pygame.draw.rect(subscreen, color, (x * tile, y * tile, tile, tile))

def draw_border():
    pygame.draw.line(screen , black , (48,73) , (48 , 525) , 2)
    pygame.draw.line(screen , black , (50,48) , (525 , 48) , 2)
    pygame.draw.line(screen , black , (525,48) , (525 , 500) , 2)
    pygame.draw.line(screen , black , (48,525) , (525 , 525) , 2)

def draw_path(path):
    for x,y in path:
        center_x =(y*tile) + 12 
        center_y =(x*tile) + 12 
        pygame.draw.circle(subscreen , pygame.Color("green") , (center_x , center_y) , 10)



font = pygame.font.Font(None , 30)
start_text = font.render("Start" , True , "Black")
end_text = font.render("End" , True , "Black")

choice1 = "Left Wall Follower"
choice2 = "Right Wall Follower"
choice3 = "Random Walk"
choice4 = "Tremaux"
choice5 = "Dijkstra"
choice6 = "A Star"
start = (0,0)
end = (18,18)
choice_text1 = font.render(choice1 , True , "Black")
choice_text2 = font.render(choice2 , True , "Black")
choice_text3 = font.render(choice3 , True , "Black")
choice_text4 = font.render(choice4 , True , "Black")
choice_text5 = font.render(choice5 , True , "Black")
choice_text6 = font.render(choice6 , True , "Black")
while True:
    show_path = False
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            # left wall following
            if 590<=mouse[0]<= 800 and 40<=mouse[1]<=90:
                show_path = True
                path,time = leftWallFollower.leftHandRule(maze , start , end)
                print(f"Time taken for Left Wall Following Algorithm: {time:.20f}")
                print(f"Path taken for Left Wall Following Algorithm: {path}")
                print()
                print()
                print()
                print()
            # right wall following
            elif 590<=mouse[0]<= 800 and 240<=mouse[1]<=290:
                show_path = True
                path,time = rightWallFollowing.solve_maze(maze , start , end)
                print(f"Time taken for Right Wall Following Algorithm: {time:.20f}")
                print(f"Path taken for Right Wall Following Algorithm: {path}")
                print()
                print()
                print()
                print()
            # random walk
            elif 590<=mouse[0]<=800 and 440<=mouse[1]<=490:
                show_path = True
                path,time = randomWalk.whatIsBroDoing(maze , start , end)
                print(f"Time taken for Random Walk Algorithm: {time:.20f}")
                print(f"Path taken for Random Walk Algorithm: {path}")
                print()
                print()
                print()
                print()
            # Dead End Filling
            elif 890<=mouse[0]<=1100 and 40<=mouse[1]<=90:
                show_path = True
                # path,time = deadEndFilling.dead_end_filling(maze , start , end)
                path,time = tremaux.runner(maze , start , end)
                print(f"Time taken for tremaux Algorithm: {time:.20f}")
                print(f"Path taken for tremaux Algorithm: {path}")
                print()
                print()
                print()
                print()
            # dijkstra
            elif 890<=mouse[0]<=1100 and 240<=mouse[1]<=290:
                show_path = True
                path,time = dikestruh.runner(maze , start , end)
                print(f"Time taken for Dijkstra Algorithm: {time:.20f}")
                print(f"Path taken for Dijkstra Algorithm: {path}")
                print()
                print()
                print()
                print()
            # a star
            elif 890<=mouse[0]<=1100 and 440<=mouse[1]<=490:
                show_path = True
                path,time = aStar.timer(maze , start , end)
                print(f"Time taken for A Star Algorithm: {time:.20f}")
                print(f"Path taken for A Star Algorithm: {path}")
                print()
                print()
                print()
                print()


   
            
    screen.fill(pygame.Color("#8cb8ff"))
    screen.blit(subscreen, (50, 50))  
    draw_maze(maze)
    if show_path:
        draw_path(path)  
    pygame.draw.rect(screen , pygame.Color("#8cb8ff") , (525,50 , 550 , 550))
    pygame.draw.rect(screen , pygame.Color("#8cb8ff") , (50,525 , 550 , 550))

    screen.blit(start_text , (10,10))
    screen.blit(end_text , (530,530))

    pygame.draw.rect(screen , pygame.Color("purple") , (590 , 40 , 210 , 50))   # 1
    pygame.draw.rect(screen , pygame.Color("purple") , (560 , 40 , 20 , 50))   # 1
    pygame.draw.rect(screen , pygame.Color("purple") , (590 , 240 , 210 , 50))  # 2
    pygame.draw.rect(screen , pygame.Color("purple") , (560 , 240 , 20 , 50))  # 2
    pygame.draw.rect(screen , pygame.Color("purple") , (590 , 440 , 210 , 50))  # 3
    pygame.draw.rect(screen , pygame.Color("purple") , (560 , 440 , 20 , 50))  # 3
    pygame.draw.rect(screen , pygame.Color("purple") , (890 , 40 , 210 , 50))   # 4
    pygame.draw.rect(screen , pygame.Color("purple") , (860 , 40 , 20 , 50))   # 4
    pygame.draw.rect(screen , pygame.Color("purple") , (890 , 240 , 210 , 50))  # 5
    pygame.draw.rect(screen , pygame.Color("purple") , (860 , 240 , 20 , 50))  # 5
    pygame.draw.rect(screen , pygame.Color("purple") , (890 , 440 , 210 , 50))  # 6
    pygame.draw.rect(screen , pygame.Color("purple") , (860 , 440 , 20 , 50))  # 6
    screen.blit(choice_text1 , (605,50))
    screen.blit(choice_text2 , (600,250))
    screen.blit(choice_text3 , (630,450))
    screen.blit(choice_text4 , (900,50))
    screen.blit(choice_text5 , (900,250))
    screen.blit(choice_text6 , (900,450))
    draw_border()
    # Blit the subscreen to the main screen
    pygame.display.update()  # Update the display
    clock.tick(30)  # Set the frame rate to 30 FPS

