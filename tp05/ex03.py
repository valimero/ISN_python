from time import time, sleep

deb = time()

i = 1
while (i < 6):
	print(i)
	sleep(1)
	i = i + 1

end = time()
print("Ce programme s'est execute en " + str(end - deb) + " seconde(s)")
