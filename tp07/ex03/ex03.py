#ex03
#Ce programme compte le nombre de mot dans le fichier mots.txt

fichier = open("mots.txt", 'r')
chaine = fichier.read()

i = chaine.count("\n")
print i
