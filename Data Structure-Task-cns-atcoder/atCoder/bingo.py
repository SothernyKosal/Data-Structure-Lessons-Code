a = [[]*3 for x in range(3)]
for x in range(3):
    ele = list(map(int, (input().split(" "))))
    a[x] = ele
N = int(input())
result = []
for x in range(N):
    key = int(input())
    for i in range(3):
        for j in range(3):
            if key == a[i][j]:
                result.append(key)
finalFalse = []
finalTrue = []
for i in range(3):
    for x in result:
        if result == []:
            finalFalse.append(False)
        if x == a[i][0] | a[i][1] | a[i][2]:
            finalTrue.append(True)
        elif x == a[i][i]:
            finalTrue.append(True)
        elif x == a[0][i] | a[1][i] | a[2][i]:
            finalTrue.append(True)
        else:
            finalFalse.append(False)
if(finalTrue==[]):
    print("No")
elif(all(finalTrue)==True):
    print("Yes")
else:
    print("No")

# code ke
# row1 = list(map(int,input().split()))
# row2 = list(map(int,input().split()))
# row3 = list(map(int,input().split()))
# n = int(input())
# arr = []
# for i in range(n):
#     temp = int(input())
#     arr.append(temp)
# #
# if row1[0] in arr and row1[1] in arr and row1[2] in arr or row2[0] in arr and row2[1] in arr and row2[2] in arr or row3[0] in arr and row3[1] in arr and row3[2] in arr:
#     print("Yes")
#     exit()
# elif row1[0] in arr and row2[0] in arr and row3[0] in arr or row1[1] in arr and row2[1] in arr and row3[1] in arr or row1[2] in arr and row2[2] in arr and row3[2] in arr:
#     print("Yes")
#     exit()
# elif row1[0] in arr and row2[1] in arr and row3[2] in arr or row1[2] in arr and row2[1] in arr and row3[0] in arr:
#     print("Yes")
#     exit()
# else:
#     print("No")
