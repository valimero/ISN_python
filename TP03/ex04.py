#ex04
#met des '*' autour de chaque caractere

mot = input("Entrer une phrase ou un mot: ")

i = 0;

while (i < len(mot)):
	print("*" + mot[i], end = '')
	i = i + 1
print("*")
