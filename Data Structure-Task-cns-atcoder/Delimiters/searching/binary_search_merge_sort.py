from fastnumbers import isfloat
import math

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def bsearch(arr,key):
    return bs_helper(arr,key,lower,upper)
def bs_helper(arr,key,lower,upper):
    mid = (lower + upper)//2
    if lower + 1 == upper:
        return None;
    if key == arr[mid]:
        return mid
    if key < arr[mid]:
        return bs_helper(arr,key,lower,mid)
    else:
        return bs_helper(arr,key,mid,upper)


# driver code to test the above code
if __name__ == '__main__':
    arr = [ 3, 13, 89, 34, 21, 44, 99, 56, 9]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

    Range = len(arr)
    if(Range%2==0): lower,upper = -1,len(arr)+1
    else: lower,upper =-1,len(arr)
    key = int(input("Enter the element you want to search: "))
    position = bsearch(arr,key)
    print(f"position of {key} is {position}")



