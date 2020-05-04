def count_occurences(s):
    occurences = s.count("gfg")
    if occurences!=0:
        return occurences
    else:
        return -1

t = int(input())
for i in range(t):
    s= input().lower()
    print(count_occurences(s))
