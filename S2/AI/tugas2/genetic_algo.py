import random
import math
import time



class Papan:
	def __init__(self, kolom, target):
		self.kolom = kolom
		self.target = int((kolom * ((kolom-1)/2)))


		self.mesa = list(range(self.kolom))
		#print(self.mesa)
		self.fitnes = 0
		self.inisial(self.kolom/2)
		self.cetak()


	def inisial(self, kolom):
		'''
		for i in range(kolom):
			rnd = random.randint(1,kolom)
			while(rnd in self.mesa):
				rnd = random.randint(1,kolom)
			self.mesa.append(rnd)
		'''

		''' swithed queen places 'count' times'''
		count = int(kolom)

		for i in range(count):
			j = random.randint(0, self.kolom - 1 )
			k = random.randint(0, self.kolom - 1 )
			#print(j, k)
			self.mesa[j], self.mesa[k] = self.mesa[k], self.mesa[j]

		# recheck fitness after moving queens
		self.cek_fitnes()


	def cek_fitnes(self):

		self.fitnes = self.target

		for i in range(self.kolom):
			for j in range(i + 1, self.kolom):
				if math.fabs(self.mesa[i] - self.mesa[j]) == j - i:
					# for each queen guarding another one reduce fitness by 1
					self.fitnes -= 1


	def cetak(self):
		for row in range(self.kolom):
			print("", end="|")
			mesa = self.mesa.index(row)
			for col in range(self.kolom):
				if col == mesa:
					print("Q", end="|")
				else:
					print("_", end="|")
			print("")



papan = []

#for x in range(4):
#	papan.append(Papan(8,28))

#print(len(papan))

while 'True':
	papan.append(Papan(8,28))


#for x in range(len(papan)):
#	print("Kombinasi Mesa : ", papan[x].mesa)
#	print("Nilai Fitnes : ", papan[x].fitnes)
#	print("Gambar Papan \n", papan[x].cetak())

#print(papan[x].mesa)
#print(papan[x].kolom)
#print(papan[x].target)
#print(papan[x].fitnes)
#print(papan[x].cetak())

"""
	def fitnes2(populasi):


		for x in populasi:
			count = 0
			for i in range(len(x)):
				for j in range(i+1, len(x)):
					#print(int(i+1), int(x[i] + x[j]))
					if math.fabs(x[i]-x[j]) == (int(j - i)):
						count += 1
						print("Diagonal -- on : ", str(int(i+1)), x[i], str(int(j+1)), x[j] )
						#print(str((int(i - j))),str(int(x[i]-x[j])))
					#print(i,x[i],j,x[j])
			healt = int((8 * (8 - 1) / 2) - count)
			print(count, healt)

start = time.time()
inisialiasi(4,4)
print(popu)
fitnes(popu)
stop = time.time()
print(stop - start)
"""
