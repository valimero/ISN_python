#ex09
#Renvoie l'identifiant de l'utilisateur

prenom = input("Quel est votre prenom ?")
nom = input("Quel est votre nom ?")

print ('\n' + "Voici votre identifiant: " + prenom.lower()[0] + nom.lower()[0:8])
