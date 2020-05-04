import time
A= [99,55,4,66,28,31,36,52,38,72]
for i in range(len(A)):
    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]
print("sorted array")
# t = time.time()
# print("time complexity",t)
for i in range(len(A)):
    print(A[i])