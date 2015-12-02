#ex03
#Programme qui affiche la chaine de caractere entree a l'envers

mot = str(input("Mot ?\n"))

i = 0
lg = int(len(mot))
while (lg > i):
	print(mot[lg - 1],  end = '')
	lg = lg - 1
