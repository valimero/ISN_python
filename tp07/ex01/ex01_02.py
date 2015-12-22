#ex01_02
# Ce programme crée un fichier et y écris 30 entiers aléatoires

import random

fichier = open("nbralea.txt", "w")
i = 0
while (i < 30):
	fichier.write(str(random.randint(0, 100)) + '\n')
	i = i + 1
fichier.close()