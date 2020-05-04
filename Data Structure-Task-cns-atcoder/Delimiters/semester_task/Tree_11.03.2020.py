class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def traverse_pre_order_recursive(root, action=print):
    if root:
        action(root.data, end=" ")
        traverse_pre_order_recursive(root.left, action)
        traverse_pre_order_recursive(root.right, action)
def traverse_pre_order_iterative(root, action=print):
    if root:
        stack = [root]
        while stack:
            node = stack.pop()
            action(node.data,end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
# root = Node("A")
# root.left = Node("B")
# root.left.left = Node("C")
# root.left.right = Node("D")
# root.right = Node("E")
# root.right.left = Node("G")
# root.right.right = Node("F")

root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
traverse_pre_order_iterative(root)