# from pythonds.basic import Stack
#
# lis = [98,23,45,14,6,67,33,42]
# lis1 = []
#
# n = len(lis)
# to_do = n-1
# did_swqp = True
# # s = Stack()
# # for i in lis:
# #     s.push(i)
# for i in range(to_do):
#     # exit(to_do=0) or not(did_swqp)
#     if i == to_do:
#         break
#     if(lis[i] > lis[i+1]):
#         lis[i], lis[i+1] = lis[i+1], lis[i]
#         b = lis.pop()
#         lis1[to_do - i] = b
# print(lis1)
#     # for i in range(to_do):
#     #     if (lis[i] > lis[i + 1]):
#     #         lis[i], lis[i + 1] = lis[i + 1], lis[i]

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]


N = int(input())
s1 = Stack()
s2 = Stack()
l = [0] * N
for _ in range(N):
    s1.push(int(input("Enter Element: ")))
for i in range(N):
    if not i % 2:
        while not s1.isEmpty():
            temp = s1.pop()
            if s2.isEmpty():
                s2.push(temp)
            else:
                if s2.peek() > temp:
                    temp2 = s2.pop()
                    s2.push(temp)
                    s2.push(temp2)
                else:
                    s2.push(temp)
        l[N - 1 - i] = s2.pop()
    else:
        while not s2.isEmpty():
            temp = s2.pop()
            if s1.isEmpty():
                s1.push(temp)
            else:
                if s1.peek() > temp:
                    temp2 = s1.pop(8)
                    s1.push(temp)
                    s1.push(temp2)
                else:
                    s1.push(temp)
        l[N - 1 - i] = s1.pop()
print(l)



