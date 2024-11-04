import pygame
import generator  # Ensure this module contains the `return_maze()` function
from solvers import leftHandRule as lfw
from solvers import dikestruh as dj
cols, rows = 19,19  # Size of the maze
tile = 25
pygame.init()
screen = pygame.display.set_mode((800, 600))
subscreen = pygame.Surface((500, 500))  # This can be used for drawing the maze
clock = pygame.time.Clock()

grey = pygame.Color("#77869e")
darkgrey = pygame.Color("#555657")
black = pygame.Color("Black")
indianred = pygame.Color("indianred2")

maze = generator.return_maze()  # Make sure this function returns a 2D list (matrix)
x = tile
y = tile



def draw_maze(matrix):
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

def reset_path(path):
    for x,y in path:
        center_x =(y*tile) + 12
        center_y =(x*tile) + 12
        pygame.draw.circle(subscreen ,grey , (center_x , center_y) , 10)

font = pygame.font.Font(None , 30)
start_text = font.render("Start" , True , "Black")
end_text = font.render("End" , True , "Black")

choice1 = "1 - Left Wall Follower"
choice2 = "2 - "
choice3 = "3 - "
choice4 = "4 - "
choice5 = "5 - "
choice6 = "6 - "
choice7 = "7 - "
start = (0,0)
end = (18,18)
choice_text1 = font.render(choice1 , True , "Black")
choice_text2 = font.render(choice2 , True , "Black")
choice_text3 = font.render(choice3 , True , "Black")
choice_text4 = font.render(choice4 , True , "Black")
choice_text5 = font.render(choice5 , True , "Black")
choice_text6 = font.render(choice6 , True , "Black")
choice_text7 = font.render(choice7 , True , "Black")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        once = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            path,time = lfw.leftHandRule(maze , start , end)
            if not once:
                print("Path taken: " , path)
                once = True
            draw_path(path)
            # pygame.display.update()
        if keys[pygame.K_2]:
            path,time = dj.runner(maze , start , end)
            draw_path(path)
        if keys[pygame.K_3]:
            pass
        if keys[pygame.K_4]:
            pass
        if keys[pygame.K_5]:
            pass
        if keys[pygame.K_6]:
            pass
        if keys[pygame.K_7]:
            print()
            print()
            print()




            
    screen.fill(pygame.Color("#8cb8ff"))
    screen.blit(subscreen, (50, 50))  
    draw_maze(maze)
    pygame.draw.rect(screen , pygame.Color("#8cb8ff") , (525,50 , 550 , 550))
    pygame.draw.rect(screen , pygame.Color("#8cb8ff") , (50,525 , 550 , 550))
    screen.blit(start_text , (10,10))
    screen.blit(end_text , (530,530))
    screen.blit(choice_text1 , (600,50))
    screen.blit(choice_text2 , (600,90))
    screen.blit(choice_text3 , (600,130))
    screen.blit(choice_text4 , (600,170))
    screen.blit(choice_text5 , (600,210))
    screen.blit(choice_text6 , (600,250))
    screen.blit(choice_text7 , (600,290))
    draw_border()
    # Blit the subscreen to the main screen
    pygame.display.update()  # Update the display
    # clock.tick(60)  # Set the frame rate to 60 FPS

