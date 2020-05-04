import time
def insertSorting(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
# t = time.time()
# print(t)
arr = [99,55,4,66,28,31,36,52,38,72]
insertSorting(arr)
print("sorted list")
for i in range(len(arr)):
    print(arr[i])