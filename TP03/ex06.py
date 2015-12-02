#ex06
#Ecris la chaine de caractere entree en remplacant une lettre sur deux par '*'

mot = input("Entrer une phrase ou un mot: ")

i = 0;

while (i < len(mot)):
	print(mot[i] + "*", end = '')
	i = i + 2
