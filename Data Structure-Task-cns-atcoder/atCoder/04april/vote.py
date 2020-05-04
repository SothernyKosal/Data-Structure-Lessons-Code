n,m = map(int,input().split())
a = list(map(int, input().split()))
popular = list(filter(lambda e: e>=(1/(4*m))*sum(a),a))
print("Yes" if len(popular) >= m else "No")