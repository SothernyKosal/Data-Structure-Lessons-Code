#
# circular_queue = []
# maxSize = int(input("Enter the size of queue: "))
#
# for i in range(1,maxSize+1):
#     circular_queue.append(i)
#
# # head = circular_queue[0]
# # tail = circular_queue[maxSize-1]
#
# print(circular_queue)
#
# ele = maxSize + 1
#
# length = len(circular_queue)
#
# if length == maxSize:
#     circular_queue.pop()
# length = len(circular_queue)
# if length < maxSize:
#     print("size of array: ",length)
#     while length < maxSize:
#         circular_queue.append(ele)
#         length += 1
#         ele += 1
# print(circular_queue)

# from queue import Queue
# q = Queue(maxsize=5)
# q._put("hello")
# for
# print(q)

class CircularQ:
    def __init__(self, size):
        self.q = [None] * size
        self.size = size
        self.count = 0
        self.top = 0
        self.tail = 0

    def enqueue(self, item):
        assert self.count < self.size, "full queue"
        self.q[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        assert self.count > 0, "empty queue"
        val = self.q[self.top]
        self.q[self.top] = None
        self.top = (self.top + 1) % self.size
        self.count -= 1
        return val


k = CircularQ(6)
k.enqueue(1)
k.enqueue(2)
print(k.dequeue())
print(k.dequeue())
k.enqueue(3)
k.enqueue(4)
k.enqueue(5)
k.enqueue(6)
k.enqueue(7)
k.enqueue(8)

print(k.dequeue())
print(k)