# Refactured 7/26/22
# made the fourier visualization to one function

# Todo:
	# Make the fourier visualization an object

import math
import pygame 


TIME = 0
PI = math.pi
SCALE = 100
time = TIME
circle_center = (250,250)

class Pos:
	def __init__(self, x,y):
		self.x = x
		self.y = y

def fourier(order,pos,scale = SCALE,circle_center = circle_center,time = TIME,surface=None):
	pos.x = int(((scale) * (4/( PI)) * (math.cos(time)))) + circle_center[0]
	pos.y = int((scale * (4/(PI)) * (math.sin(time)))) + circle_center[0]
	tmp = (pos.x, pos.y)
	if surface:
		pygame.draw.circle(surface,(255,255,255),circle_center,_computation(100, 1),1)
		pygame.draw.line(surface,(255,255,255),circle_center,(pos.x,pos.y))

	for i in range(1,order):
		i=i*2+1
		pos.x += int(((scale) * (4/(i * PI)) * (math.cos(i*time)))) 
		pos.y += int((scale * (4/(i * PI)) * (math.sin(i*time))))

		if surface:
			pygame.draw.circle(surface,(255,255,255),(tmp[0], tmp[1]),_computation(scale,i),1)
			pygame.draw.line(surface,(255,255,255),(tmp[0],tmp[1]),(pos.x,pos.y))
			tmp = (pos.x, pos.y)

		
	return (pos.x,pos.y)


def _computation(scale,i):
	return int(scale*(4/(i*math.pi)))


if __name__ == '__main__':
	
	pos = Pos(250,250)
	scale = 100
	i,j = 0,0
	while i < 7:
		four = fourier(7,pos, scale)
		pos.x = four[0]
		pos.y = four[1]
		print(four)
		TIME-=0.004
		i +=1
	print("============================")
