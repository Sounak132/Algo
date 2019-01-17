lst = [int (x) for x in input("Enter your Un_sorted array elements separated by a space:\n").split(" ")]
size = len(lst)
#B = [56,45,79,90,345,33,1,-12,68] --- Test_case

def partition(A,start,end):
    pivot_index = start
    pi = A[end]
    for i in range (start,end):
        if(A[i]<pi):
            A[pivot_index],A[i]=A[i],A[pivot_index]
            pivot_index+=1
    A[pivot_index],A[end]=A[end],A[pivot_index]
    return pivot_index
            
def quick_sort(A,start,end):
    
    if (start <end):
        pivot_index=partition(A,start,end)
        quick_sort(A,start,pivot_index-1)
        quick_sort(A,pivot_index+1,end)
    
    return A

p= quick_sort(lst,0,len(lst)-1)

print("Here is your sorted array \n",p)