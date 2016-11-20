import math

MAX = raw_input('Masukkan Maksimal Bilangan : ')

MAX = int(MAX)

STOP = int(math.ceil(math.sqrt(MAX)))

#print STOP
print 'Daftar Bilangan Prima dari 0 ke %i adalah' % MAX

PRIMES = [True] * MAX
PRIMES[0] = 'False'

#print 'PRIME[0]',PRIMES[0]

for i in range(1, MAX):
	PRIMES[i] = 'True'

for i in range(0, STOP):
	if PRIMES[i] == 'True':
		for j in range(1, (MAX/2)):
			PRIMES[(i*j)] = 'False'

for i in range(1, MAX):
	if PRIMES[i] == 'True':
#		print 'Daftar Bilangan Prima dari 0 ke %i adalah' % MAX
		print 'Angka : ', i
