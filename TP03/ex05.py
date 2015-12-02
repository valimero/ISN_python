#ex05
#ecris deux fois chaque caractere de la chaine entree

mot = input("Entrer une phrase ou un mot: ")

i = 0;

while (i < len(mot)):
	print(mot[i], end = '')
	print(mot[i], end = '')
	i = i + 1
