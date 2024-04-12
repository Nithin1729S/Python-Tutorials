
def insertionSort(lst):
    for i in range(1,len(lst)):
        j=i-1
        x=lst[i]
        while lst[j]>x and j>-1:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=x
    print(lst)

lst=[45,2,34,1,1,8,0]
insertionSort(lst)












