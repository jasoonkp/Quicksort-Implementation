
from random import randint

# defines array
numArray = [0]*25


# generates random array
for i in range(0,25):
    numArray[i] = randint(1,100)


# swap 2 values in array method
# parameters are array, and indices used to swap elements
def swapValues(numArray,i,j):
    numArray[i], numArray[j] = numArray[j], numArray[i]


# prints array method
def printArray(numArray):
    r = len(numArray) 
    for i in range(0,r):
        print(numArray[i], end = " ")
    
    print("")


# partioning method
# var i is greater than pivot, var j is less than pivot
def Partition(numArray,l,r):
    i = l - 1

    pivot = randint(l,r)
    swapValues(numArray,pivot,r)
    for j in range(l,r):
        if numArray[j] <= numArray[r]:
            swapValues(numArray,j,i+1)
            i += 1
    swapValues(numArray, r,i+1)
    return i + 1


# quicksort method (recursive)
def Quicksort(numArray,l,r):
    printArray(numArray)
    print("")

    if l >= r:
        return
    q = Partition(numArray,l,r)
    Quicksort(numArray,l,q-1)
    Quicksort(numArray,q+1,r)


 



def main():
    printArray(numArray)
    swapValues(numArray, 1 ,2)
    Quicksort(numArray,0,len(numArray)-1)
    printArray(numArray)

if __name__ == "__main__":
    main()