class kendaraan:
	def __init__(self,jenis,cc,roda):
		self.jenis = jenis
		self.cc = cc
		self.roda = roda
	
	#def jenis(self, jenis):
	#	self.jenis = jenis

	#def cetak(self):
	#	print ('Jenis Kendaraan : "%s" ' % self.jenis)
	#	print ('Jumlah CC : "%i" cc' % self.cc)
	#	print ('Jumlah Roda : "%i" buah' % self.roda)
	
	def cc(self,cc):
		self.cc = cc

	def roda(self,roda):
		self.roda = roda


class roda2(kendaraan):
	def __init__(self,jenis,cc):
		self.jenis = jenis
		self.cc = cc
		self.roda = 2

	def cetak(self):
		print ('Jenis Kendaraan : "%s" ' % self.jenis)
		print ('Jumlah CC : "%i" cc' % self.cc)
		print ('Jumlah Roda : "%i" buah' % self.roda)

	def jenis(self, jenis):
		self.jenis = jenis


class mobil(kendaraan):
	def __init__(self,jenis,cc,roda,pintu):
		self.jenis = jenis
		self.cc = cc
		self.roda = roda
		self.pintu = pintu

	def jenis(self, jenis):
		self.jenis = jenis

	def pintu(self,pintu):
		self.pintu = pintu

	def cetak(self):
		print ('Jenis Kendaraan : "%s" ' % self.jenis)
		print ('Jumlah CC : "%i" cc' % self.cc)
		print ('Jumlah Roda : "%i" buah' % self.roda)
		print ('Jumlah Pintu : "%i" buah' % self.pintu)
