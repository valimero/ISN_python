#ex03
from time import time, sleep

def print_time():
	""" Cette fonction affiche les entiers de 1 a 5 en faisant une pause \
	de 1 secondes entre les affichages et affiche le temps mis par l'execution de cette fonction """
	deb = time()		# Stocke l'instant t au lancement du programme

	i = 1
	while (i < 6):
		print(i)
		if i != 5: 		# Pour ne pas avoir de pause après l'affichage du dernier caractère
			sleep(1)
		i = i + 1
		
	end = time()		# Stocke l'instant t a la fin du programme pour permettre le calcul du temps d'éxécution.
	print("Cette fonction s'est executee en " + str(end - deb) + " seconde(s)")

#dev
print_time()
