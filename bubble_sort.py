lst = [int (x) for x in input("Enter your Un_sorted array elements separated by a space:\n").split(" ")]
size = len(lst)
def bubble_sort(lst, size):
    for i in range(size):
        for j in range (size-1):
            if (lst[j]>lst[j+1]):
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

print("Here is your sorted array in ascending order\n",bubble_sort(lst,size))