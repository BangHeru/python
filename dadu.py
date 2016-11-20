import random
dadu = []
dadu.append("" +
	"[=======]\n" +
	"[       ]\n" +
	"[   0   ]\n" +
	"[       ]\n" +
	"[=======]\n")

dadu.append(
	"[=======]\n" +
	"[0      ]\n" +
	"[       ]\n" +
	"[      0]\n" +
	"[=======]\n")

dadu.append(
	"[=======]\n" +
	"[0      ]\n" +
	"[   0   ]\n" +
	"[      0]\n" +
	"[=======]\n")

dadu.append(
	"[=======]\n" +
	"[0     0]\n" +
	"[       ]\n" +
	"[0     0]\n" +
	"[=======]\n")

dadu.append(
	"[=======]\n" +
	"[0     0]\n" +
	"[   0   ]\n" +
	"[0     0]\n" +
	"[=======]\n")

dadu.append(
	"[=======]\n" +
	"[0     0]\n" +
	"[0     0]\n" +
	"[0     0]\n" +
	"[=======]\n")


def kocok():
	cb= 0
	while 'True':

		angka1 = random.randint(1,6)
		angka2 = random.randint(1,6)
		angka3 = random.randint(1,6)
		cb += 1
		print(angka1, angka2, angka3)
		if angka1 == angka2 and angka3 == angka2:
			print('*'*cb)
			print('JACKPOT !!!!!!')
			print('Percobaan %i' % cb)
			print(dadu[(angka1)-1])
			print(dadu[(angka2)-1])
			print(dadu[(angka3)-1])
			print('*'*cb)
			return False
		else:
			print(dadu[(angka1) - 1])
			print(dadu[(angka2) - 1])
			print(dadu[(angka3) - 1])

kocok()
