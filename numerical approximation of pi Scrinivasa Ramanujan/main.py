"Approximaton of the inverse of pi 1/3.1475432....."
from math import *

const = (2 * sqrt(2))/9801
sumation = 0
for k in range(200):
	sumation+=(factorial(4*k)*(1103+(26390*k)))/(((factorial(k))**4)*(396**(4*k)))

result = const*sumation
print('Actual value: ', 1/pi)
print('Approximaton: ', result)