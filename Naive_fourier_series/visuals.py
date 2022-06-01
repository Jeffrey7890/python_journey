"""
Date: 5/6/2021
Fourier Series by Ogwu Jeffrey

Fourier Series for Square wave functions.

Just so you know, I hard coded it no function or lazy stuff. ;)

Date: 6/1/2022
Looking at this, now i feel like pewking, :( 
This Code has a lot of repeatations, lack of use of
objects and functions, need refacturing.

"""

import pygame
import math

pygame.init()

color = pygame.Color(255,255,255,0)
background_color = pygame.Color(0,0,0,0)

width = 1200
height = 400

screen = pygame.display.set_mode((width,height))
screen.fill(background_color)

surface = pygame.Surface((width,height))
surface2 = pygame.Surface((width/2,height))

surface2.fill(background_color)

x = 250
y = 250
time = 0

circle_center = (250,250)
radius = 100

wave =[] #To append all the points of the y4 axis
run = True

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	#First order
	x = int((100*(4/math.pi))*math.cos(time))+circle_center[0]
	y = int((100*(4/math.pi))*math.sin(time))+circle_center[1]


	#Second order
	x2 = int((100*(4/(3*math.pi)))*math.cos(3*time))+x
	y2 = int((100*(4/(3*math.pi)))*math.sin(3*time))+y


	#Third order
	x3 = int((100*(4/(5*math.pi)))*math.cos(5*time))+x2
	y3 = int((100*(4/(5*math.pi)))*math.sin(5*time))+y2


	#Fourth order
	x4 = int((100*(4/(7*math.pi)))*math.cos(7*time))+x3
	y4 = int((100*(4/(7*math.pi)))*math.sin(7*time))+y3

	x5 = int((100*(4/(9*math.pi)))*math.cos(9*time))+x4
	y5 = int((100*(4/(9*math.pi)))*math.sin(9*time))+y4

	x6 = int((100*(4/(11*math.pi)))*math.cos(11*time))+x5
	y6 = int((100*(4/(11*math.pi)))*math.sin(11*time))+y5

	x7 = int((100*(4/(13*math.pi)))*math.cos(13*time))+x6
	y7 = int((100*(4/(13*math.pi)))*math.sin(13*time))+y6

	wave.append(y7)

	surface.fill(background_color)
	pygame.draw.circle(surface,(color),circle_center,int(100*(4/math.pi)),1)
	pygame.draw.line(surface,(color),circle_center,(x,y))


	index =500
	s = -1
	for i in range(len(wave)):
		pygame.draw.circle(surface,(color),(index+i,wave[s]),1)
		# surface.set_at((index+i,wave[s]),(255,255,255))
		s-=1
	# surface.set_at((x7+200,y7+200),(255,255,255))


	pygame.draw.line(surface,(color),(x7,y7),(index,wave[i]))


	if len(wave) == 700:
		wave.clear()

	#Drawing each circle 
	pygame.draw.circle(surface,(color),(x,y),int(100*(4/(3*math.pi))),1)
	pygame.draw.line(surface,(color),(x,y),(x2,y2))

	pygame.draw.circle(surface,(color),(x2,y2),int(100*(4/(5*math.pi))),1)
	pygame.draw.line(surface,(color),(x2,y2),(x3,y3))

	pygame.draw.circle(surface,(color),(x3,y3),int(100*(4/(7*math.pi))),1)
	pygame.draw.line(surface,(color),(x3,y3),(x4,y4))

	pygame.draw.circle(surface,(color),(x4,y4),int(100*(4/(9*math.pi))),1)
	pygame.draw.line(surface,(color),(x4,y4),(x5,y5))


	pygame.draw.circle(surface,(color),(x5,y5),int(100*(4/(11*math.pi))),1)
	pygame.draw.line(surface,(color),(x5,y5),(x6,y6))


	pygame.draw.circle(surface,(color),(x6,y6),int(100*(4/(13*math.pi))),1)
	pygame.draw.line(surface,(color),(x6,y6),(x7,y7))
	pygame.draw.circle(surface,(color),(x7,y7),3)


	time-=0.04#Ajust time between 0.01 - 0.7 for faster wave and shorter wave length

	screen.blit(surface,(0,0))
	pygame.display.flip()
pygame.quit()
