import re
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

valStack = Stack()
def suffixEva(postfix):
    for token in postfix.split():
        if re.match(r'[^\+\-\*\/\%\^\(\)]', token):
            valStack.push(token)
        else:
            operation = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b,
                '%': lambda a, b: a % b,
                '^': lambda a, b: a ** b,
            }
            b = int(valStack.pop())
            a = int(valStack.pop())
            c = operation[token](a, b)
            valStack.push(c)
        print(valStack.stack)
    return int(valStack.pop())

suffix = input('suffix:\n')
print(suffixEva(suffix))