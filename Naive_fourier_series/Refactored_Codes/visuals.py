"""
Date: 5/6/2021
Fourier Series by Ogwu Jeffrey

Fourier Series for Square wave functions.

Just so you know, I hard coded it no function or lazy stuff. ;)

Refactured by Ogwu Jeffrey: 7/26/22

"""

import pygame
import math
from fourier import Pos, fourier

pygame.init()

color = pygame.Color(255,255,255,0)
background_color = pygame.Color(0,0,0,0)

width = 1200
height = 400

screen = pygame.display.set_mode((width,height))
screen.fill(background_color)

surface = pygame.Surface((width,height))

x = 250
y = 250
time = 0

circle_center = (250,250)
radius = 100

wave =[] #To append all the points of the y4 axis

run = True
pointPosition = Pos(x,y)

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	surface.fill(background_color)

	test_y = fourier(7,Pos(pointPosition.x, pointPosition.y),100,circle_center,time,surface)
	pointPosition.x = test_y[0]
	pointPosition.y = test_y[1]
	wave.append(pointPosition.y)

	index =500
	s = -1
	for i in range(len(wave)):
		pygame.draw.circle(surface,(color),(index+i,wave[s]),1)
		s-=1

	pygame.draw.line(surface,(color),(pointPosition.x,pointPosition.y),(index,wave[i]))


	if len(wave) == 700:
		wave.clear()


	time-=0.01#Ajust time between 0.01 - 0.7 for faster wave and shorter wave length

	screen.blit(surface,(0,0))
	pygame.display.flip()
pygame.quit()
