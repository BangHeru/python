

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        print(key)
        #Insert A[j] into the sorted sequence A[1....j-1]
        i = j - 1
        while (i > 0) and (A[i] > key):
            A[i+1] = A[i]
            print(A[i+1])
            i = i - 1



        A[i+1] = key
        #print(key)



list = [5, 2, 4, 6, 4, 2, 1, 3]
list.sort()
print(list)
#insertion_sort(list)