class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None

    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node
    def insert_before(self, ref_node, new_node):
        self.9
    def insert_beg(self):

    def insert_at_end(self):
    def remove(self):
    def display(self):