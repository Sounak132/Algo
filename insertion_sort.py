lst = [float (x) for x in input("Enter your Un_sorted array elements separated by a space:\n").split(" ")]
size = len(lst)

def insertion_sort(lst,size):
    for i in range(size):
        a = i
        while(a>=1):
            if (lst[a]<lst[a-1]):
                lst[a],lst[a-1]=lst[a-1],lst[a]
            else:
                break
            a-=1
    return lst
print("Here is your sorted array in ascending order\n",insertion_sort(lst,size))