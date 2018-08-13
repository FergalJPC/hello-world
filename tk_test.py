import pygame

pygame.init()

width = 300
lenght = 300

size = width, lenght

screen = pygame.display.set_mode(size)

red = (255, 0, 0)


gameRunning = True

x = 20
y = 20

clock = pygame.time.Clock()

FPS = 30


while gameRunning:
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameRunning = False





	vol_y = 10


	y += vol_y



	if y == lenght:



		y -= vol_y 
		vol_y = 0

	


	screen.fill((255,255,255))

	pygame.draw.rect(screen,  red, [width/2, y, 10, 10])

	pygame.display.flip()

	clock.tick(FPS)
		
	