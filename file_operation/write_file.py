namaFile = 'demo.csv'
modeAkses = 'w'

file = open(namaFile,modeAkses)


def fibo(n):
    p = 1
    q = 1

    file.write('0,' + str(p) +'\n')
    file.write('1,' + str(q)+'\n')


    for i in range(2, n-1):
        r = p + q
        p = q
        q = r
        file.write(str(i) +',' +str(r) +'\n')
        file.close()


fibo(100)
