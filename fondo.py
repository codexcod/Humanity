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



screen = pygame.display.set_mode((600, 600))

pasto = pygame.Surface((100,100))
pasto.fill((0,255,0),None,0)

montaña = pygame.Surface((100,100))
montaña.fill((80,40,0),None,0)

agua = pygame.Surface((100,100))
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

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                  posX -= 1

            if event.key == pygame.K_RIGHT:
                posX += 1

         
            if event.key == pygame.K_UP:
                posY -= 1

            if event.key == pygame.K_DOWN:
                posY += 1

    if posY >= 7:
      posY = 7
  
    if posY <= 3:
      posY = 3

    if posX >= 7:
      posX = 7
  
    if posX <= 3:
      posX = 3

    forX= 0
    for y in range(posX - 3,posX + 3):
      forY=0
      for x in range(posY - 3, posY + 3):
        if(matrix[x][y] == 1):
          screen.blit(pasto, (forX * 100,forY * 100))

        if(matrix[x][y] == 0):
          screen.blit(montaña, (forX * 100,forY * 100))   
          
        if(matrix[x][y] == 2):
          screen.blit(agua, (forX * 100,forY * 100))      

        forY += 1

      forX += 1
      
         

    pygame.display.update()
    



