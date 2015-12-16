#ex08

import random

def mdp(N):
	"""Cette fonction genere un mot de passe"""

	chaine = "qwertyuiopasdfghjklmzxcvbnQWERTYUIOPASDFGHJKLMZXCVBN0123456789"
	str_mdp = ""
	i = 0
	while (i < N):
		str_mdp = str_mdp + chaine[random.randint(0, 61)]
		i = i + 1
	return(str_mdp)

#dev
print(mdp(1))
