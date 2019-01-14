array = [int (x) for x in input("Input the un-sorted array elemments one by one separated by spaces\n").split(" ")]

length = len(array)
for i in range(length-1):
    a=i
    for j in range(i,length):
        if(array[a]>array[j]):
            a=j
    array[a],array[i]=array[i],array[a]
print("Here is your sortde array in ascending order\n",array)