from random import randint
import time

# defines array
numArray = [0]*100000


# generates random array
for i in range(0,100000):
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
 #  printArray(numArray)

    while l < r:
        q = Partition(numArray,l,r)

    # Tail-Recursion Elimination (optimization to speed algoritm up)
        if (q-1) < (r - q):
            Quicksort(numArray,l,q-1)
            l = q + 1
        else:
            Quicksort(numArray,q+1,r)
            r = q - 1


 



def main():
    print("unsorted: ",end=" " )
    printArray(numArray)
    start = time.time()
    Quicksort(numArray,0,len(numArray)-1)
    end = time.time()
    print("sorted:   ",end=" " )
    printArray(numArray)
    print("time it took to execute:", end - start, " seconds")

if __name__ == "__main__":
    main()