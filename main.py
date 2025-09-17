
from random import randint

# defines array
numArray = [0]*25

# generates random array

for i in range(0,25):
    numArray[i] = randint(1,100)

#prints array
def printArray(numArray):
    r = len(numArray) 
    for i in range(0,r):
        print(numArray[i])

def Partition(numArray,l,r):
    m = randint(l,r)
    numArray[m], numArray[r] = numArray[r], numArray[m]
    print("test")


def Quicksort(numArray,l,r):
    print(numArray[0])

    r = len(numArray)
    l = 0
    if r <= l:
        return
    q = Partition(numArray,l,r)
    Quicksort(numArray,l,q-1)
    Quicksort(numArray,q+1,r)


 



def main():
    printArray(numArray)

if __name__ == "__main__":
    main()