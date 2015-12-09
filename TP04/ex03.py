#ex03
#Ce programme trie une liste: Si un nom a moins de 6 caractère le stocke dans 
#la liste 'a' sinon il le stocke dans la liste 'b'

# --- Declaration des variables ---
nom = ["Michel", "Jacques", "Toto", "Lea"]
a = []
b = []
i = 0

# --- Trie les noms ---
while (i < len(nom)): #dev
	if (len(nom[i]) < 6):
		a.append(nom[i])
	else:
		b.append(nom[i])
	i = i + 1

#dev
print(a, b)
