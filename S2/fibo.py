def fibo(n):
    p = 1
    q = 1

    print ("0", p)
    print ("1", q)

    for i in range(2, n + 1):
        r = p + q
        p = q
        q = r
        print (i, r)


#n = int(input("Jumlah n Fibo : "))
#fibo(n)