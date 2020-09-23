def radie(area):
	import math

	return math.sqrt(area/math.pi)


area = float(input('Area: '))
print(f'Radie: {radie(area)}')
