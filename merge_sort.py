lst = [int (x) for x in input("Enter your Un_sorted array elements separated by a space:\n").split(" ")]
size = len(lst)
#Defining a function to merge two sub arrays to its mother array//
def merge(R,L,A):
    r = len(R)
    l = len(L)
    length = r+l
    i=0
    j=0
    a=0
    while (i<l and j<r):
        if L[i]<R[j]:
            A[a] = L[i]
            i+=1
        else:
            A[a] = R[j]
            j+=1
        a+=1
    if i==l:
        A[a:]=R[j:].copy()
    if j==r:
        A[a:]=L[i:].copy()
    return A
# Calling the recursive function //
def merge_sort(lst):
    if(len(lst)<2):
        return lst
    m = len(lst)//2
    L = lst[:m]
    R = lst[m:]
    merge_sort(L)
    merge_sort(R)
    merge(L,R,lst)
    return lst

print("Here is your sorted array in ascending order \n",merge_sort(lst))    
