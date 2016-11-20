namaFile = 'demo.txt'
modeAkses = 'r'
lst = []
file = open(namaFile,modeAkses)

for data in file:
    lst.append(data.split())

file.close()

for value in lst:
    print(value[0] + " panjang " + str(len(value[1])))