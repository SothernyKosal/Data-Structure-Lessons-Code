t = int(input())
for i in range(2):
    # print(i)
    lenn = int(input())
    # print(lenn)
    ls = list(map(int, input().split(" ")))

    for i in range(len(ls)):
        # print(i)
        if i == lenn -1 :
            break
        else:

            if ls[i] == ls[i+1]:
                # print(ls[i], " : ", ls[i + 1])
                # print(i, "=> ", i + 1)
                ls.remove(ls[i])
                ls.append(0)
            elif ls[i] == ls[i-1]:
                # print(ls[i], " : ", ls[i + 1])
                # print(i, "=> ", i + 1)
                ls.remove(ls[i])
                ls.append(0)
            else:
                if ls[i+1] != ls[i]  & lenn -1 == i:
                    # print(ls[i], ls[i+1], ls[i-1])
                    ls.remove(ls[i+1])
                    ls.append(0)
    # print(ls)
    print(sum(ls))