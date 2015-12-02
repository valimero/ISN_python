#ex04
#Programme qui affiche les n mutlitples de 7

n = int(input("N ?\n"))
i = 1 

while (i < 100):
	if (i * 7 <= n):
		print(str(i * 7), end='')
		if ((i * 7) % 4 == 0):
			print('*', end='')
		print(" ", end = '')
		i = i + 1
	else:
		break
