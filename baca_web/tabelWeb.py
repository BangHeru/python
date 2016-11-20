import urllib
import urllib.request
from bs4 import BeautifulSoup
import time


namaFile = 'data.csv'
modeAkses = 'w'
print ("Waktu Mulai : ", time.asctime( time.localtime(time.time()) ))
print('\n')
file = open(namaFile,modeAkses,encoding='utf8')

def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata


kd_paket = []
paket = []
hps = []
tahapan = []
kategori = []
lst_kategori = []
jenis = []
metode = []

lengkap = []


#def ambil_data():
for x in range(1,22,1):
	soup = make_soup("http://lpse.acehtengahkab.go.id/eproc/lelang.gridtable.pager/"+str(x)+"?s=5")

	# ambil kode paket
	for nama in soup.find_all('b'):
		for lnk in nama.find_all('a'):
			#print(link.get('href'))
			kd = lnk.get('href')
			akhir = kd.find(';')
			kd_paket.append(kd[19:akhir])

	#ambil nama paket
	for nama in soup.find_all('b'):
		for lnk in nama.find_all('a'):
			#lnk = lnk
			paket.append((lnk.text).strip())

	#ambil tahap lelang
	for nama in soup.find_all("td", class_="tahap"):
		for lnk in nama.find_all('a'):
			tahapan.append(nama.text)

	#ambil nilai HPS
	for nama in soup.find_all('td', class_="pkt_hps"):
		for lnk in nama.find_all('span'):
			hps.append(lnk.text)

	#ambil kategori lelang
	for tahap in soup.find_all("div", class_="list"):
		for nama in tahap.find_all('span'):
			kategori.append(nama.text)

	for x in range(len(kategori)):
		tulisan = kategori[x]

		if tulisan == "Kategori":
			lst_kategori.append(kategori[(x+2)])
		elif tulisan == "Jenis Lelang":
			jenis.append(kategori[(x+2)])
		elif tulisan == "Metode":
			metode.append(kategori[(x+2)])

file.write("Kode Paket" + "\t" +"Nama Paket" + "\t" + "tahapan Sekarang" + "\t" + "Nilai HPS"+ "\t" + "Kategori Lelang"+ "\t" + "Jenis Lelang"+ "\t" + "Metode Lelang"+"\n")

for x in range(len(paket)):
	lengkap.append(kd_paket[x] + "\t" + paket[x] + "\t" + tahapan[x] + "\t" + hps[x]+ "\t" + lst_kategori[x]+ "\t" + jenis[x]+ "\t" + metode[x])
	file.write(kd_paket[x] + "\t" + paket[x].strip() + "\t" + tahapan[x] + "\t" + hps[x] + "\t" + lst_kategori[x]+ "\t" + jenis[x] + "\t" + metode[x] + "\n")


print(len(lengkap))

print ("\nWaktu Selesai : ", time.asctime( time.localtime(time.time()) ))

file.close()