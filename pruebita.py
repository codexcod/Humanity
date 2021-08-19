import pygame

pygame.init()

matrix = [
[2,2,2,2,2,2,2,2,2,2],
[2,1,1,1,1,1,1,1,1,2],
[2,1,1,1,1,1,1,1,1,2],
[2,1,1,1,0,0,0,1,1,2],
[2,1,1,1,3,3,3,1,1,2],
[2,1,1,1,1,1,1,1,1,2],
[2,1,1,1,1,1,1,1,1,2],
[2,1,1,1,1,1,1,1,1,2],
[2,1,1,1,1,1,1,1,1,2],
[2,2,2,2,2,2,2,2,2,2]]



screen = pygame.display.set_mode((1000, 600))

pasto = pygame.Surface((100,100))
pasto.fill((0,255,0),None,0)

montaña = pygame.Surface((100,100))
montaña.fill((80,40,0),None,0)

agua = pygame.Surface((40,40))
agua.fill((0,0,240),None,0)

posX = 5
posY = 5

running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(agua,(0,0))
    screen.blit(agua,(40,0))
    screen.blit(agua,(80,0))

         

    pygame.display.update()
    



