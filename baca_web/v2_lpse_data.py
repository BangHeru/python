import urllib
import urllib.request
from bs4 import BeautifulSoup
import time


namaFile = 'data2.csv'
modeAkses = 'w'
print ("Waktu Mulai : ", time.asctime( time.localtime(time.time()) ))
file = open(namaFile,modeAkses,encoding='utf8')

def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata

kd_paket = []
paket = []
hps = []
pagu = []
tahapan = []
kategori = []
jenis = []
metode = []
dokumen = []
evaluasi = []
kualifikasi = []
anggaran = []
skpk = []
lengkap = []
tahun2 ="2016"
y = 1
#def ambil_data():
#for x in range(1,6,1):
while (tahun2 == "2016"):

	soup = make_soup("http://lpse.acehtengahkab.go.id/eproc/lelang.gridtable.pager/"+str(y)+"?s=5")
	y += 1
	#ambil nama kode paket
	for nama in soup.find_all('b'):
		for lnk in nama.find_all('a'):
			kd = lnk.get('href')
			akhir = kd.find(';')
			kdp = str(kd[19:akhir])
			#print(str(kdp))
			print(tahun2)
			kd_paket.append(kdp)

#for z in range(0,len(kd_paket),1):
			sementara = []
			soup2 = make_soup("http://lpse.acehtengahkab.go.id/eproc/lelang/view/" + str(kdp) + "/")
			#y += 1
			for data in soup2.find_all("td"):
				#print(data.text)
				sementara.append(data.text)
				#for lnk in data.find_all('td', colspan_="3"):
				#    print(lnk.text)
				#    skpk.append(lnk.text)

			for x in range(len(sementara)):
				tulisan = sementara[x]
				if tulisan == "Satuan Kerja":
					#print(str(sementara[(x+1)]))
					skpk.append(str(sementara[(x+1)]))
				elif tulisan == 'Kategori':
					#print(str(sementara[(x + 1)]))
					kategori.append(str(sementara[(x + 1)]))
				elif tulisan == 'Metode Pengadaan':
					#print(str(sementara[(x + 1)]))
					metode.append(str(sementara[(x + 1)]))
				elif tulisan == 'Metode Kualifikasi':
					#print(str(sementara[(x + 1)]))
					kualifikasi.append(str(sementara[(x + 1)]))
				elif tulisan == 'Metode Dokumen':
					#print(str(sementara[(x + 1)]))
					dokumen.append(str(sementara[(x + 1)]))
				elif tulisan == 'Metode Evaluasi':
					#print(str(sementara[(x + 1)]))
					evaluasi.append(str(sementara[(x + 1)]))
				elif tulisan == 'Anggaran':
					#print(str(y) + " " +str(sementara[(x + 1)]))
					tahun = str(sementara[(x + 1)])
					tahun2 = tahun[:4]
					#y += 1
					anggaran.append(str(sementara[(x + 1)]))
				elif tulisan == 'Nilai Pagu Paket':
					#print(str(sementara[(x + 1)]))
					pagu.append(str(sementara[(x + 1)]))
				elif tulisan == 'Nilai HPS Paket':
					#print(str(sementara[(x + 1)]))
					hps.append(str(sementara[(x + 1)]))

			for data in soup2.find_all("b"):
				for nama in data.find_all('strong'):
					#print(lnk.text)
					nma = (nama.text).replace("\n","")
					paket.append(nma.strip())

			for data in soup2.find_all("td"):
				for lnk in data.find_all('a', class_="jpopup"):
					#print(lnk.text)
					tahapan.append(lnk.text)




#print(len(kategori))


"""
file.write("Nomor" + "\t" + "Kode Paket" + "\t" +"Nama Paket" + "\t" + "Tahapan Sekarang" + "\t" +
		   "SKPK"+ "\t" + "Kategori Lelang"+ "\t" + "Metode Pengadaan"+ "\t" +
		   "Metode Kualifikasi"+ "\t" + "Metode Dokumen" +  "\t" + "Metode Evaluasi"+ "\t" +
		   "Sumber Dana" + "\t" + "Pagu Anggaran" + "\t" + "HPS" + "\n")
"""

for x in range(len(paket)):

	lengkap.append(kd_paket[x] + "\t" + paket[x] + "\t" + tahapan[x] + "\t" + skpk[x]+ "\t" +
	kategori[x]+ "\t" + metode[x]+ "\t" + kualifikasi[x] + "\t" + dokumen[x] + "\t" + evaluasi[x] + "\t" +
	anggaran[x] + "\t" + pagu[x] + "\t" + hps[x])

	"""
	file.write(str(int(x+1)) + "\t" + kd_paket[x] + "\t" + paket[x].strip() + "\t" + tahapan[x].strip() + "\t" + skpk[x].strip() + "\t" +
			   kategori[x].strip() + "\t" + metode[x].strip() + "\t" + kualifikasi[x].strip() + "\t" +
			   dokumen[x].strip() + "\t" + evaluasi[x].strip() + "\t" + anggaran[x].strip() + "\t" +
			   pagu[x] + "\t" + hps[x] + "\n")
	"""

for x in lengkap:
	print(x)

#print(len(lengkap))

print ("\nWaktu Selesai : ", time.asctime( time.localtime(time.time()) ))


file.close()
