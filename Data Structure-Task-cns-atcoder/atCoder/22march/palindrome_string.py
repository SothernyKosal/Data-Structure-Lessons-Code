S  = input()
N = len(S)
n1,n2 = ((N-1)/2),(N+3)/2
n1,n2 = int(n1),int(n2)
sh,st = S[:n1],S[n2-1:N]

if sh == sh[::-1] and st == st[::-1] and S==S[::-1]:
    print("Yes")
else:
    print("No")

