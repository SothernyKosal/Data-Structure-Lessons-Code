t = int(input())
for i in range(t):
    col_len = list(map(int, input().split(" ")))
    row1 = list(map(int, input().split(" ")))
    row2 = list(map(int, input().split(" ")))
    sum1 = sum(row1)
    sum2 = sum(row2)
    if sum1 > sum2:
        print("C1")
    else:
        print("C2")

