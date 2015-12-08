#ex09
#Renvoie l'identifiant de l'utilisateur

prenom = input("Quel est votre prenom ?\n")
nom = input("\nQuel est votre nom ?\n")

print ('\n' + "Voici votre identifiant: " + prenom.lower()[0] + nom.lower()[0:8])
