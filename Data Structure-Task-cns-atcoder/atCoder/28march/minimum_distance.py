# k,n= list(map(int,input().split(" ")))
# dis = list(map(int,input().split(" ")))
# # d1,d2,d3 = dis[0],dis[1],dis[2]
# maxdis = k-dis[-1] + dis[0]
# for i in range(n):
#     if dis[]
#
# min_dis = int(d2-d1) + int(d3 - d2)
# print(min_dis)
k,n = map(int, input().split())
lst = list(map(int, input().split()))

maxDis = (k-lst[-1]) + lst[0]
for i in range(n-1):
  if lst[i+1] - lst[i] > maxDis:
    maxDis = lst[i+1] - lst[i]
print(k-maxDis)