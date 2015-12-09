from time import time, sleep

deb = time()		# Stocke l'instant t au lancement du programme

i = 1
while (i < 6):
	print(i)
	if i != 5: 		# Pour ne pas avoir de pause après l'affichage du dernier caractère
		sleep(1)
	i = i + 1

end = time()		# Stocke l'instant t a la fin du programme pour permettre le calcul du temps d'éxécution.

print("Ce programme s'est execute en " + str(end - deb) + " seconde(s)")
