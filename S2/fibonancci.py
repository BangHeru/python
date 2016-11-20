def fib(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)	
		print(a, end=' ')
		#print(a)
		a, b = b, a+b
	#print()
	return result

while True:
	print('Input angka 0 (nol) untuk keluar')
	angka = int(input('Masukkan Maksimal Angka Fibo : '))
	if angka == 0:
		break
	else:
		print('Hasil Fibo sampai dengan %i', angka)
		fib(angka)
		print ('\n=====================')
