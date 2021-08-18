import pygame

pygame.init()

matrix = [
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1]]

screen = pygame.display.set_mode((500, 500))

pasto = pygame.Color(0,255,0)

posX = 5
posY = 5

running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(posX - 2,posX + 2):
      for y in range(posY - 2, posY + 2):
        screen.blit(pasto, (x,y))
         

    pygame.display.update()
    



