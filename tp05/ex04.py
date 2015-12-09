#ex04
def fonction():
# --- Demande a l'utilisateur une chaine de caractere et le caractere a comparer ---
	chaine = str(input("Entrer une chaine de caractere."))
	char = str(input("Entrer le caractere a compter"))

# --- Initialise les variable ---
	r = 0
	i = 0

# --- Cherche le caractere dans la chaine et augmente r de 1 si il est present ---
	while (i < len(chaine)):
		if(chaine[i] == char[0]):
			r = r + 1
		i = i + 1
	return (r)

# dev
print(fonction())
