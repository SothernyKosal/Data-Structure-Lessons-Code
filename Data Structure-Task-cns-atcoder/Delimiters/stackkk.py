class Stack:

    def __init__(self) -> object:
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.item

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top.next
        self.top = self._top.next
        self._size -= 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1

class _StackNode:
    def __int__(self, item, link):
        self.item = item
        self.next = link

prompt = "Enter an int value"
stack = Stack()
value = int(input(prompt))
while value >= 0:
    stack.push(value)
    value = int(input(prompt))
print(value)
while not stack.isEmpty():
    value = stack.pop(value)
    print(value)
