#ex09
# Cet exercice demande à l'utilisateur les températures de 7 jours, fait la
# moyenne et l'affiche


# --- Declaration des Variables ---
i = 0
jour = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
temp = [0, 0, 0, 0, 0, 0, 0]
r = 0

# --- Demande à l'utilisateur la température et la stocke dans la variable de 
# type liste "temp"
while (i < 7):
	temp[i] = float(input ("Quelle est la temperature de " + jour[i] + " ?"))
	i = i + 1

i = 0		# Remet le compteur i à 0 pour pouvoir le réutiliser


# --- Calcul la moyenne des température entrée ---
while (i < 7):
	r = r + temp[i]
	i = i + 1

# --- Affiche la moyenne sur la sortie standard ---
print ("La temperature moyenne des 7 jours est : " + str(r / 7))

#Fin du programme
