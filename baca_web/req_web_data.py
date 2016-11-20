import requests
from bs4 import BeautifulSoup
import time

#
class lpse:
	def __init__(self, url, mulai, sampai):
		self.url = url
		self.mulai = mulai
		self.sampai = sampai
		self.kode = []
		self.datax = ''

		self.ambil_kode()
		self.ambil_data()


	def ambil_kode(self):
		x = 1
		text = ""
		print ("Waktu Mulai \t: ", time.asctime( time.localtime(time.time()) ))
		print(self.url)
		while ('True'):
			url = self.url + '/eproc/lelang.gridtable.pager/' + str(x) + '?s=5'
			#url = 'http://lpse.acehutara.go.id/eproc/lelang.gridtable.pager/'+str(x)+'?s=5'
			r = requests.get(url)
			if (text != r.text):
				text = r.text
				soup = BeautifulSoup(r.text, 'html.parser')
				for tds in soup.find_all('b'):
					for lnk in tds.find_all('a'):
						link = lnk.get('href')
						#print(link[19:])
						self.kode.append(link[19:])
				x += 1

			else:
				#self.ambil_data()
				print("Waktu Selesai \t: ", time.asctime(time.localtime(time.time())))
				break


	def cetak(self):
		print(self.datax)


	def ambil_data(self):
		namaFile = 'data2.csv'
		#modeAkses = 'w'

		file = open(namaFile, 'w', encoding='utf8')

		judul = ("Kode Paket" + "\t" + "Nama Paket" + "\t" + "Tahapan Sekarang" + "\t" +
				 "SKPK" + "\t" + "Kategori Lelang" + "\t" + "Metode Pengadaan" + "\t" +
				 "Metode Kualifikasi" + "\t" + "Metode Dokumen" + "\t" + "Metode Evaluasi" + "\t" +
				 "Sumber Dana" + "\t" + "Pagu Anggaran" + "\t" + "HPS" + "\n")
		file.write(judul)

		print("Waktu Mulai \t: ", time.asctime(time.localtime(time.time())))

		while(True):
			for x in self.kode:
				self.datax = x
				sementara = []
				url = self.url + '/eproc/lelang/view/'+str(x)
				r = requests.get(url)
				soup = BeautifulSoup(r.text, 'html.parser')
				self.cetak()
				for data in soup.find_all("td"):
					#print(data.text)
					sementara.append(data.text)
				thn = sementara[23]
				thn = int(thn[:4])
				#if (thn > tahun):
				#	pass

				if (thn == self.mulai or thn <= self.sampai):
					data = (str(x) + "\t" + sementara[3].strip() + "\t" + sementara[7].strip() + "\t" +
							sementara[11].strip() + "\t" + sementara[13].strip() + "\t" + sementara[15].strip() + "\t" +
							sementara[17].strip() + "\t" + sementara[19].strip() + "\t" + sementara[21].strip() + "\t" +
							sementara[23].strip() + "\t" + sementara[25].strip() + "\t" + sementara[
								27].strip() + "\t" + "\n")
					file.write(data)
					#lengkap.append(data)
					#print("Waktu Selesai \t: ", time.asctime(time.localtime(time.time())))
					#return False

				if (thn == '' or thn < self.mulai or x == self.kode[-1]):
					print("Waktu Selesai \t: ", time.asctime(time.localtime(time.time())))
					return False

		file.close()


	#print("Waktu Selesai \t: ", time.asctime(time.localtime(time.time())))




grab = lpse('http://lpse.acehtengahkab.go.id',2015,2016)
#grab.ambil_kode()
#grab.ambil_data()

#gsgsg gjhgasd hjagdashjd

"""
0 -> Kode Lelang
1 -> 1196296
2 -> Nama Lelang
3 -> Belanja Bahan dan Alat Peraga Kampanye
4 -> Keterangan
5 ->
6 -> Tahap Lelang Saat ini
7 -> Surat Penunjukan Penyedia Barang/JasaPenandatanganan Kontrak
8 -> Agency
9 -> Pemerintah Kabupaten Aceh Tengah
10 -> Satuan Kerja
11 -> Komisi Independen Pemilihan Kab. Aceh Tengah
12 -> Kategori
13 -> Pengadaan Barang
14 -> Metode Pengadaan
15 -> e-Lelang Sederhana
16 -> Metode Kualifikasi
17 -> Pascakualifikasi
18 -> Metode Dokumen
19 -> Satu File
20 -> Metode Evaluasi
21 -> Sistem Gugur
22 -> Anggaran
23 -> 2016 - APBN
24 -> Nilai Pagu Paket
25 -> Rp 1.370.200.000,00
26 -> Nilai HPS Paket
27 -> Rp 1.027.650.000,00
28 -> Jenis Kontrak
29 -> Cara PembayaranHarga SatuanPembebanan Tahun AnggaranTahun TunggalSumber PendanaanPengadaan Tunggal
30 -> Cara Pembayaran
31 -> Harga Satuan
32 -> Pembebanan Tahun Anggaran
33 -> Tahun Tunggal
34 -> Sumber Pendanaan
35 -> Pengadaan Tunggal
36 -> Kualifikasi Usaha
37 -> Perusahaan Kecil
38 -> Lokasi Pekerjaan
39 -> Kabupaten Aceh Tengah - Aceh Tengah (Kab.)
40 -> Syarat Kualifikasi
41 -> *Ijin UsahaIjin UsahaKlasifikasiSITUSurat Izin Tempat Usaha yang masih berlakuTDPTanda Daftar Perusahaan yang masih berlakuTDITanda Daftar Industri yang masih berlakuSIUPSurat Izin Usaha Perdagangan yang masih berlaku dengan klasifikasi percetakan atau KBLI yang sesuaiNPWPNomor Pokok Wajib PajakAkte PerusahaanAkte Pendirian Perusahaan dan Perubahan (apabila ada)*Telah melunasi kewajiban pajak tahun terakhir2015*Memiliki kemampuan untuk menyediakan fasilitas/peralatan/perlengkapan pemasangan di lapangan sesuai LDP*Memiliki Pengalaman Pekerjaan
42 -> *
43 -> Ijin UsahaIjin UsahaKlasifikasiSITUSurat Izin Tempat Usaha yang masih berlakuTDPTanda Daftar Perusahaan yang masih berlakuTDITanda Daftar Industri yang masih berlakuSIUPSurat Izin Usaha Perdagangan yang masih berlaku dengan klasifikasi percetakan atau KBLI yang sesuaiNPWPNomor Pokok Wajib PajakAkte PerusahaanAkte Pendirian Perusahaan dan Perubahan (apabila ada)
44 -> Ijin Usaha
45 -> Klasifikasi
46 -> SITU
47 -> Surat Izin Tempat Usaha yang masih berlaku
48 -> TDP
49 -> Tanda Daftar Perusahaan yang masih berlaku
50 -> TDI
51 -> Tanda Daftar Industri yang masih berlaku
52 -> SIUP
53 -> Surat Izin Usaha Perdagangan yang masih berlaku dengan klasifikasi percetakan atau KBLI yang sesuai
54 -> NPWP
55 -> Nomor Pokok Wajib Pajak
56 -> Akte Perusahaan
57 -> Akte Pendirian Perusahaan dan Perubahan (apabila ada)
58 -> *
59 -> Telah melunasi kewajiban pajak tahun terakhir2015
60 -> *
61 -> Memiliki kemampuan untuk menyediakan fasilitas/peralatan/perlengkapan pemasangan di lapangan sesuai LDP
62 -> *
63 -> Memiliki Pengalaman Pekerjaan
64 -> Peserta Lelang
65 -> 18 peserta  [Detil...]
66 ->
"""