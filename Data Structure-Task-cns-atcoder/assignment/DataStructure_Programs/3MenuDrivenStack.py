from numpy import ndarray

maxSize = 5
top = -1
stack = ndarray((maxSize),int)

def push(item,top):
    if top == maxSize-1:
        print("Stack is overflow")
    stack[top] = item
    return
def pop():
    if(top == -1):
        print("Stack is underflow")
        return -1;
    item = stack[top]
    return item
def display(top):
    if(top == -1):
        print("Stack is empty")
        return
    print("Stack element are: ")
    while top >= 0:
        print(f'| {stack[top]} |')
        top -= 1
    print("\t\t---------")
def palindrome(top):
    flag = 1
    print("Stack content are:")
    i = top
    while i>=0:
        print(f'| {stack[i]} |')
        i -= 1
    print("Reverse of stack content are:")
    for i in range(0,top+1):
        print(f'| {stack[i]} |')
    for i in range(0, top//2):
        if(stack[i] != stack[top-i]):
            flag = 0
            break
        i+=1
    if flag == 1:
        print("Palindrome number")
        print("\t\t---------")
    else:
        print("isn't palindrome")
        print("\t\t---------")

menu = "~~~~~~Menu~~~~~~"
print("\t\t",menu)
print("1. Push an element on a Stack and overflow demonstration")
print("2. Pop an element to a Stack and underflow demonstration")
print("3. Check the stack is Palindrome or not")
print("4. Display the status of Stack")
print("5. Exit the program")
while(1):
    choice = int(input("Enter your choice:"))

    if (choice == 1):
        item = int(input("Enter element to be pushed:"))
        print("\t\t---------")
        top+=1
        push(item, top)
    elif(choice == 2):
        # item = int(input("Enter element to be pop:"))
        item = pop()
        if(item!= -1):
            print("Element popped is :",item)
            print("\t\t---------")
        top -= 1
    elif(choice == 3):

        palindrome(top)

    elif(choice == 4):
        display(top)
    elif(choice == 5):
        print("exit the menu")
        break
    else:
        print("invalid choice")
        break








