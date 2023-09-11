def partition(L,start,stop):
    pivot = L[start]
    wall = start

    for scout in range(start+1,stop+1):
        if L[scout] < L[pivot]:
            wall = wall + 1
            L[wall] , L[scout] = L[scout] , L[wall]
    
    L[wall] , L[start] = L[start] , L[wall]
    return wall

def quicksort(L,start,stop):
    if start >= stop:
        return
    p = partition(L,start,stop)
    quicksort(L,start,p-1)
    quicksort(L,p+1, stop)




