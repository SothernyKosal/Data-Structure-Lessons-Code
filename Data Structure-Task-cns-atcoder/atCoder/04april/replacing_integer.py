n,k = list(map(int,input().split()))
if n%k==0:
    print(0)
else:
    l = [n]
    p = n//k
    c = n - (k*p)
    half = k//2
    while c > half:
        c = abs(c-k)
    l.append(c)
    print(min(l))
