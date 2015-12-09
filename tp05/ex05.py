def sym(chaine):
	""" Cette fonction inverse une chaine et retourne la chaine inversee """
	chaine2 = []
	i = 0
	while(i < len(chaine)):
		chaine2.append(chaine[len(chaine)  - (1+i)])
		i = 1 + i
	return chaine2

def palindrome(chaine):
	""" Cette fonction verifie si une chaine est un palindrome et retourne un entier ( 1 si oui, 0 si non)"""
	i = 0
	while (i < len(chaine)):
		if not (chaine[i] == chaine[len(chaine) - (1+i)]):
			return(0)
		i = i + 1
	return(1)


#dev
print(palindrome("1233211"))
