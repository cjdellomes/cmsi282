def lcm(x, y):
	return (x * y) / gcd(x,y)

def gcd(x, y):
	while(y):
		x, y = y, x % y
	return x