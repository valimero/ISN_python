def f(x):
	"""Reproduit la fonction f"""
	if(x < 1):
		return(2*x -3)
	if(1 <= x < 2):
		return(3*x + 2)
	if(x >= 2):
		return(x - 4)

def g(x, y):
	""" Reproduit la fonction g"""
	return((1/(x*x) + 1/(y*y)))


#dev
print(g(1, 2))
