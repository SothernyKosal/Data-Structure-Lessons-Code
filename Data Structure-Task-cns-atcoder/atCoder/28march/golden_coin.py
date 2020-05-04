x = int(input())
happiness_point=0
while x>=500:
        happiness_point+=1000
        x-=500
while x>=5:
    happiness_point+=5
    x-=5

print(happiness_point)