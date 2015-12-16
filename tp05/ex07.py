#ex07
#Cette fonction simule n lancers de dés bien équilibrés et retourne une liste contenant les résultats du tirage.
import random

def simuldes(n):
	liste = []
	i = 0
	while(i<n):
		liste.append(random.randint(1, 6))
		i = i + 1
	return(liste)


#dev
print(simuldes(5))

