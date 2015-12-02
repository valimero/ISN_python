#exercice 05
#Cet exercice demande l'age de l'utilisateur et l'ecrit sur la sortie standard

nom = "coucou"

nom = str(input("Nom ?\n"))
age = int(input("\nAge ?\n"))
print("\nBonjour " + nom + '\n' + "Plus que " + str(100 - age) + " ans pour etre centenaire !\n" )
