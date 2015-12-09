#ex04
#Ce programme cherche le nombre le plus grand dans une liste

# --- Decalration des variables ---
L = [12, 23, 66, 6666, 7787, 44, 23, 12]
i = 0
r = L[0]

# --- cherche le nombre le plus grand de la liste et l'affecte a la variable 
# de type entier 'r' ---
while (i < len(L)):
	if (L[i] > r):
		r = L[i]
	i = i + 1

print(r)
