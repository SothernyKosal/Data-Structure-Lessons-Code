arr = [10,20,30,40,50]
print("Original array")
for i in arr:
    print(i)

def insert(position,ele):
    arr[position] = ele
def delete(position):
    arr.pop(position)

add_index = int(input("Enter index to add an element: "))
ele_to_add = int(input("Enter element to add: "))
insert(add_index,ele_to_add)
print(f"after add element to a valid position: {arr}")

del_index = int(input("Enter index to delete: "))
delete(del_index)
print(f"after delete an element form a valid position: {arr}")
