# from array import Array
# N = int(input("Enter N number of element of array: "))
# menu = [2,4,7]
# index,value = int(input("insert the index:")),int(input())
# menu[index] = menu[index+1]
# menu[index+1] = menu[index+2]
# menu[index] = value
# print(menu)

# menu[2] = 3
# print(menu)
# print(len(menu))
# menu.append(1)
# menu.append(3)
# menu.append(4)
# res = '#'.join(str(i) for i in menu)
# print(res)
#
# print("helo"+str(3))
# lis = [1,2,3,5]
# for i in lis:
#     print(i)

choice = True
arr = []
while choice == True:
    print(arr)
    insertElement = int(input("How many element do you want to insert: "))
    for i in range(insertElement):
        arr.append(input())
    print(' '.join(str(x) for x in arr))
    insertIndex = int(input(("which index do you want to replace of inserting:")))
    value =  int(input("input the value: "))
    arr[insertIndex] = value
    print(' '.join(str(x) for x in arr))
    indexDelete = int(input("Which index do you want to remove: "))
    remove = arr.pop(indexDelete)
    print(arr)
    inputChoice = input("do you want to continue or not y/n: ")
    if inputChoice == 'N' or inputChoice == 'n':
        choice = False





