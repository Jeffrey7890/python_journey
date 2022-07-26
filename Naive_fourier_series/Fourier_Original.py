import math

def fourier(time):
	for i in range(0,5):
		i=i*2+1
		result = (4*math.sin(i*time))/(i*math.pi)
		result2 = (4*math.cos(i*time))/(i*math.pi)

		print(result,result2)

fourier(0.05)
