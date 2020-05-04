import collections
dic = dict()
n = int(input())

for i in range(n):
    survey = input().split(" ")
    dic[survey[0]] = survey[1]

listOfElems = list(dic.values())

# Create a dictionary of elements & their frequency count
dictOfElems = dict(collections.Counter(listOfElems))
# Remove elements from dictionary whose value is 1, i.e. non duplicate items
greater = 0
greater_key = ""

for key, value in dictOfElems.items():
    if value > greater:
        greater = value
        greater_key = key
    if value == greater_key:
        greater_key = "no most like"
print(greater_key)
print(listOfElems.count("football"))


