class circularQ:
    def __init__(self, size):
        self.q = [None] * size
        self.size = size
        self.count = 0
        self.front = 0
        self.rear = 0
    def enqueue(self,item):
        assert self.count < self.size, "queue is full"
        self.q[self.rear] = item
        self.rear =( self.rear + 1)% self.size
        self.count += 1
    def dequeue(self):
        assert self.count > 0, "queue is empty"
        val = self.q[self.front]
        self.q[self.front] = None
        self.front = (self.front +1 ) % self.size
        self.count -= 1
        return val

cirQ = circularQ(5)
print("Your circular queue's size is 5.")
print("1. Insert an element and overflow queue\n"\
      "2. delete an element and underflow queue\n"\
      "3. display queue\n"\
      "4. Exit the program\n")

while (1):
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if cirQ.count == cirQ.size:
            print("queue is overflow")
            continue
        item = int(input("Enter an item to enqueue: "))
        cirQ.enqueue(item)
        print("\t\t---------")

    elif choice == 2:
        if cirQ.count == 0:
            print("queue is underflow")
            continue
        de = cirQ.dequeue()
        print(de)
        print("\t\t---------")

    elif choice == 3:
        if cirQ.count == 0:
            print("Empty queue")
            break
        for i in cirQ.q:
            if i == None:
                continue
            print(i)
        print("\t\t---------")

    elif choice == 4:
        print("exit")
        break

