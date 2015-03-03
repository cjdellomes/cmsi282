def exponentMod(b, c, p):
	return (b ** c) % (p - 1)

def primaryMod(a, b, c, p):
	return (a ** exponentMod(b, c, p)) % p