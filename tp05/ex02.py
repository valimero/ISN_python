def zeta(x, n):
	""" reproduit la fonction zeta """
	k = 0
	r = 0.0
	t = 0.0
	puissance = 0
	while(k < n):
		t = k**x
		if not (t == 0):
			r = r + 1 / t
		k = k + 1
	return (r)

print(zeta(4, 1))
print(zeta(2, 19))
