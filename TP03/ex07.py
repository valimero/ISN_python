#ex07
#Remplace les voyelle de la chaine entree part "*" et les espaces part "_._"

mot = input("Entrer une phrase ou un mot: ")

i = 0
lg = len(mot)

while (i < lg):
	if (mot[i] == 'a' or mot[i] == 'e' or mot[i] == 'i' or mot[i] == 'o' or \
		mot[i] == 'u' or mot[i] == 'y' or mot[i] == 'A' or mot[i] == 'E' or \
		mot[i] == 'I' or mot[i] == 'O' or mot[i] == 'U' or mot[i] == 'Y'):
		print('*', end = '')
	elif (mot[i] == ' '):
		print("_._", end = '')
	else:
		print(mot[i], end = '')
	i = i + 1;
