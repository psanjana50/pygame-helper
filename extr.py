import pygame

pygame.init()

screen=pygame.display.set_mode((700,600))

pyi=pygame.image.load("spaceship.png") #load image
pyi=pygame.transform.scale(pyi,(64,64)) #resize image


playing=True
while playing:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            playing=False
        elif event.type==pygame.KEYDOWN and event.key == pygame.K_a:
            screen.blit(pyi,(318,526))
        elif event.type==pygame.KEYUP and event.key == pygame.K_a:
            pyi.set_alpha(20)
        elif event.type==pygame.KEYUP and event.key != pygame.K_a:
            print(pygame.KEYUP.text)
        else: 
            
            print("passed")
    pygame.display.update()