lst = [int (x) for x in input("Enter your Un_sorted array elements separated by a space:\n").split(" ")]
size = len(lst)

def counting_sort(A):
    maxi = max(A)
    mini = min(A)
    length = maxi - mini +1
    #---initializing
    Sum_count=[0 for i in range(length)]
    Sorted_array=[0 for i in range(len(A))]
    Index = [int(x) for x in range(mini,maxi+1)]
    Count=[]
    #---sorting
    for i in range(length):
        Count.append(A.count(Index[i]))
    Sum_count[0]=Count[0]
    for i in range(1,length):
        Sum_count[i]=Sum_count[i-1]+Count[i]
    for i in range(len(A)):
        Sorted_array[Sum_count[A[i]-mini]-1]=A[i]
        Sum_count[A[i]-mini]-=1
    return Sorted_array
print("Here is your sorted array\n",counting_sort(lst))