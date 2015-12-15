#ex06
import sys
import random

def des6():
	"""Cette fonction affiche le résultat du tirage d'un dés à 6 faces bien équilibré
tant que l'utilisateur appuie sur la touche entrée, quitte le programme quand 
l'utilisateur entre \"q\" """

	while(input() != 'q'):
		print(random.randint(1, 6))
	sys.exit()

#dev
des6()
