#ex02
# Ce programme trie une liste, met les nombres pairs dans une liste et les
# impairs dans une autre

# --- Declaration des variables ---
L = [0, 1, 3, 54, 6, 8, 6]
pair = []
impair = []
i = 0

# --- Permet de trier la liste ---
while (i < len(L)):
	if(L[i] % 2 == 0):
		pair.append(L[i])
	else:
		impair.append(L[i])
	i = i + 1

print(pair, impair)
