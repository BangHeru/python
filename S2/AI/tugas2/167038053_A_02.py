import random
import math
import copy

class buat_papan:
    def __init__(self, ukuran, target):
        self.ukuran = ukuran
        self.target = target

        self.fitnes = 0
        self.mesa = list(range(self.ukuran))
        self.acak(self.ukuran / 2)


    def acak(self, ulang):
        ulang = int(ulang)

        for i in range(ulang):
            j = random.randint(0,self.ukuran - 1)
            k = random.randint(0, self.ukuran - 1)

            self.mesa[j], self.mesa[k] = self.mesa[k], self.mesa[j]

        self.cek_fitnes()


    def acak_ulang(self):
        self.acak(2)

        if random.uniform(0, 1) < 0.25:
            self.acak(1)


    def cek_fitnes(self):
        self.fitnes = self.target

        for i in range(self.ukuran):
            for j in range(i + 1, self.ukuran):
                if math.fabs(self.mesa[i] - self.mesa[j]) == j - i:
                    self.fitnes -= 1


    def cetak_papan(self):
        for baris in range(self.ukuran):
            print("", end='|')

            mesa = self.mesa.index(baris)

            for kol in range(self.ukuran):
                if kol == mesa:
                    print("Q", end='|')
                else:
                    print("_", end='|')
            print("")



class gen_algo:
    def __init__(self, ukuran, jum_populasi):
        self.ukuran = ukuran
        self.jum_populasi = jum_populasi

        self.jum_generasi = 1
        self.target = int((self.ukuran * (self.ukuran - 1)) / 2)


        self.populasi = []

        self.proses_awal()

        while True:
            if self.target_tercapai() == True:
                break

            self.proses_selanjutnya()

        if self.target_tercapai():
            print("Jawaban didapat pada percobaan ke %s" % self.jum_generasi)
            for populasi in self.populasi:
                if populasi.fitnes == self.target:
                    print(populasi.mesa)
                    populasi.cetak_papan()


    def target_tercapai(self):
        for populasi in self.populasi:
            if populasi.fitnes == self.target:
                return True

            return False

    def proses_awal(self):
        for i in range(self.jum_populasi):
            self.populasi.append(buat_papan(self.ukuran, self.target))

        self.cetak_populasi()


    def seleksi_acak(self):
        lis_populasi = []
        for i in range(len(self.populasi)):
            lis_populasi.append((i, self.populasi[i].fitnes))
        lis_populasi.sort(key=lambda pop_item: pop_item[1], reverse=True)

        return lis_populasi[:int(len(lis_populasi) / 3)]


    def proses_selanjutnya(self):
        self.jum_generasi += 1

        seleksi = self.seleksi_acak()

        populasi_baru = []
        while len(populasi_baru) < self.jum_populasi:
            sel = random.choice(seleksi)[0]
            populasi_baru.append(copy.deepcopy(self.populasi[sel]))

        self.populasi = populasi_baru

        for populasi in self.populasi:
            populasi.acak_ulang()

        self.cetak_populasi(seleksi)


    def cetak_populasi(self, seleksi=None):
        print("Populasi #%d" % self.jum_generasi)

        if seleksi == None:
            seleksi = []

        print("       Menggunakan id ke : %s dari populasi sebelumnya" % str([sel[0] for sel in seleksi]))

        i = 0
        for populasi in self.populasi:
            print("%8d : (%d) %s" % (i, populasi.fitnes, str(populasi.mesa)))
            i += 1



if __name__ == '__main__':
    ukuran = int(input("Ukuuran Papan : "))
    populasi = int(input("Jumlah Populasi : "))

    gen_algo(ukuran,populasi)