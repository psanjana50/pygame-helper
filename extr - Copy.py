import pygame
import random
pygame.init() # intialize the application

screen=pygame.display.set_mode((400,400)) # set display size

pygame.display.set_caption("Ready")

screen.fill(color=(155,1,1))

quit=True
while quit:
    
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
            quit=False 
            
        elif event.type == pygame.KEYDOWN: 
            # print(event.key) #press and get the code for pressed key
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)
            screen.fill(color=(r,g,b))
            pygame.display.update()
            
        else:
            pass
        
        pygame.display.update()
        
        
        
        
        
        